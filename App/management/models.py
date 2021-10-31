# Django Import:
from django.utils.translation import gettext_lazy as _
from django.dispatch import receiver
from django.db import models

# Applications Import:
from .managers import ActiveManager

# Validators Import:
from .validators import ColorValidator


# Additional device models:
class Tag(models.Model):
    # Validators:
    color_validator = ColorValidator()
    # Model values:
    name = models.CharField(max_length=32, blank=False, unique=True)
    color = models.CharField(
        max_length=8,
        blank=True,
        null=True,
        validators=[color_validator],
        help_text=_('Hexadecimal representation of colour, for example #73a6ff.'),
        error_messages={
            'null': _('This field is mandatory.'),
            'blank': _('This field is mandatory.'),
            'invalid': _('Enter the correct colour value. It must be a 3/6 character hexadecimal number with # on begining'),
        },
    )
    description = models.CharField(max_length=512, default="Color description")
    devices = models.ManyToManyField('Device', through="TagDeviceRelation")

    def __str__(self) -> str:
        return self.name


class Credential(models.Model):
    # Creation data:
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Username data:
    name = models.CharField(max_length=32, blank=False, unique=True)
    username = models.CharField(max_length=64, blank=False)
    description = models.CharField(max_length=512, default="Device credential description")

    # Security data:
    password = models.CharField(max_length=64, null=True)
    secret = models.CharField(max_length=64, null=True, blank=True)
    token = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


# Relations models:
class TagDeviceRelation(models.Model):
    device = models.ForeignKey('Device', on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [['device', 'tag']]


# Device related models:
class Device(models.Model):
    PATH = 'static/management/svg/'
    STATUS_CHOICES = (
        (0, _('Nonactive')),
        (1, _('Active')),
        (2, _('ToBin')),
    )
    DEVICE_TYPE = (
        (0, _('autodetect')),
        (1, _('cisco_ios')),
        (2, _('cisco_xr')),
        (3, _('cisco_xe')),
        (4, _('cisco_nxos')),
    )
    ICO = (
        (0, (f'{PATH}router.svg')),
        (1, (f'{PATH}asa-5500.svg')),
        (2, (f'{PATH}atm-router.svg')),
        (3, (f'{PATH}cisco-asa-5500.svg')),
        (4, (f'{PATH}director-class-fibre-channel-di.svg')),
        (5, (f'{PATH}firewall-service-module-fwsm.svg')),
        (6, (f'{PATH}firewall.svg')),
        (7, (f'{PATH}generic-gateway.svg')),
        (8, (f'{PATH}ios-firewall.svg')),
        (9, (f'{PATH}layer-3-switch.svg')),
        (10, (f'{PATH}nexus-2000-fabric-extender.svg')),
        (11, (f'{PATH}nexus-5000.svg')),
        (12, (f'{PATH}nexus-7000.svg')),
        (13, (f'{PATH}route-switch-processor.svg')),
        (14, (f'{PATH}router-firewall.svg')),
        (15, (f'{PATH}accesspoint.svg')),
        (16, (f'{PATH}wireless-router.svg')),
        (17, (f'{PATH}workgroup-switch.svg')),
        (18, (f'{PATH}cloud.svg')),
        (19, (f'{PATH}fibre-channel-fabric-switch.svg')),
        (20, (f'{PATH}ground-terminal.svg')),
        (21, (f'{PATH}mesh-ap.svg')),
        (22, (f'{PATH}modem.svg')),
        (23, (f'{PATH}netflow-router.svg')),
        (24, (f'{PATH}telecommuter-house.svg')),
        (25, (f'{PATH}vpn-gateway.svg')),
        (26, (f'{PATH}wavelength-router.svg')),
    )

    # Creation and status data:
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Device data:
    name = models.CharField(max_length=32, blank=False, unique=True)
    hostname = models.CharField(
        max_length=64,
        blank=False,
        unique=True,
        error_messages={
            'null': _('This field is mandatory.'),
            'blank': _('This field is mandatory.'),
            'unique': _('This field must be unique.'),
        },
        help_text=_('Enter a valid IP address or hostname.'),
    )
    device_type = models.IntegerField(choices=DEVICE_TYPE, default=0)
    ico = models.IntegerField(choices=ICO, default=0)
    ssh_port = models.IntegerField(default=22)
    https_port = models.IntegerField(default=443)
    description = models.CharField(max_length=512, default="Device description")

    # Security and credentials:
    credential = models.ForeignKey(Credential, on_delete=models.PROTECT, null=True, blank=True)
    secret = models.CharField(max_length=64, null=True)
    token = models.CharField(max_length=128, null=True)
    certificate = models.BooleanField(default=False)

    # Device status:
    ssh_status = models.BooleanField(default=False)
    https_status = models.BooleanField(default=False)
    ping_status = models.BooleanField(default=False)

    # Object managers:
    objects = models.Manager()
    active = ActiveManager()

    def __str__(self) -> str:
        return self.name

@receiver(models.signals.post_save, sender=Device)
def execute_after_save(sender, instance, created, *args, **kwargs):
    if created:
        # Check if device is available:
        pass


class DeviceData(models.Model):

    # Corelation witch device model:
    device = models.ForeignKey(Device, on_delete=models.CASCADE, null=False, blank=False)
    
    # Creation data:
    created = models.DateTimeField(auto_now_add=True)

    # Basic device information:
    hostname = models.CharField(max_length=64, blank=True, null=True)
    system_version = models.CharField(max_length=64, blank=True, null=True)
    domain_name = models.CharField(max_length=64, blank=True, null=True)
    default_gateway = models.GenericIPAddressField(blank=True, null=True)
    name_server_list = models.JSONField(blank=True, null=True)
    ntp_server_list = models.JSONField(blank=True, null=True)
    os_boot_files_list = models.JSONField(blank=True, null=True)
    ios_users_list = models.JSONField(blank=True, null=True)

    # SNMP protocol information:
    snmp_server_community_list = models.JSONField(blank=True, null=True)
    snmp_server_group_list = models.JSONField(blank=True, null=True)
    snmp_server_user_list = models.JSONField(blank=True, null=True)

    # STP protocol information:
    spanning_tree_mode = models.CharField(max_length=64,blank=True,null=True)

    # 