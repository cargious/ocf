class ControllerMappings():

	@staticmethod
	def getConditionMappings():
		conditionMappings = {
					#SERVER mappings

					"server.name":"metaObj.server.get_name()",
					#"server.id":"metaObj.server.get_id()",
					#"server.uuid":"metaObj.server.get_uuid()",
					#"server.operating_system_version":"metaObj.server.get_operating_system_version()",
					#"server.operating_system_distribution":"metaObj.server.get_operating_system_distribution()",
					#"server.virtualization_type":"metaObj.server.get_virtualization_type()",
					"server.status":"metaObj.server.get_status()",
					
					#VM mappings
					#XXX: This mappings only alows ONE virtual machine in the xml, otherwise the metaObj parameters of the others vms will not be evaluated
					
					"number.vms":ControllerMappings.getNumberOfVMs,	
				 	"vm.name": "metaObj.server.virtual_machines[0].get_name()",
                                	#"vm.uuid": "metaObj.server.virtual_machines[0].get_uuid()",
					"vm.status":"metaObj.server.virtual_machines[0].get_status()",
					#"vm.project_id":"metaObj.server.virtual_machines[0].get_project_id()",
					"vm.project_name":"metaObj.server.virtual_machines[0].get_project_name()",
					#"vm.slice_id":"metaObj.server.virtual_machines[0].get_slice_id()",
					"vm.slice_name": "metaObj.server.virtual_machines[0].get_slice_name()",
					"vm.operating_system_type":"metaObj.server.virtual_machines[0].get_operating_system_type()",
					"vm.operating_system_version":"metaObj.server.virtual_machines[0].get_operating_system_version()",
					"vm.operating_system_distribution":"metaObj.server.virtual_machines[0].get_operating_system_distribution()",
					"vm.virtualization_type":"metaObj.server.virtual_machines[0].get_virtualization_type()",
					#"vm.server_id":"metaObj.server.virtual_machines[0].get_server_id()",
					
					#XEN configuration mappings
					
					#DEPRECATED:XXX"vm.hd_size_mb": "vt_manager.controller.policies.ControllerMappings.getValueFromConfiguration(metaObj,'metaObj.server.virtual_machines[0]',eval('metaObj.server.virtual_machines[0].get_virtualization_type()'),'get_hd_size_mb()')",
					"vm.hd_size_mb":ControllerMappings.getVMHDMemory,

					#DEPRECATED:XXX"vm.hd_size_mb": "metaObj.server.virtual_machines[0].xen_configuration.get_hd_size_mb()",
					#"vm.hd_origin_path":"metaObj.server.virtual_machines[0].xen_configuration.get_hd_origin_path()",
					#"vm.configurator":"metaObj.server.virtual_machines[0].xen_configuration.get_configurator()",

					"vm.memory_mb": ControllerMappings.getVMMemory,
					
					
					#DEPRECATED:XXX"vm.memory_mb":"metaObj.server.virtual_machines[0].xen_configuration.get_memory_mb()",
					
					#INTERFACES mappings
					
					#"vm.xen_conf.interfaces.name":"metaObj.server.virtual_machines[0].xen_configuration.interfaces.interface[0].get_name()",
					#"vm.xen_conf.interfaces.mac":"metaObj.server.virtual_machines[0].xen_configuration.interfaces.interface[0].get_mac()",
					#"vm.xen_conf.interfaces.ip":"metaObj.server.virtual_machines[0].xen_configuration.interfaces.interface[0].get_ip()",
					#"vm.xen_conf.interfaces.mask":"metaObj.server.virtual_machines[0].xen_configuration.interfaces.interface[0].get_mask()",
					#"vm.xen_conf.interfaces.gw":"metaObj.server.virtual_machines[0].xen_configuration.interfaces.interface[0].get_gw()",
					#"vm.xen_conf.interfaces.dns1":"metaObj.server.virtual_machines[0].xen_configuration.interfaces.interface[0].get_dns1()",
					#"vm.xen_conf.interfaces.dns2":"metaObj.server.virtual_machines[0].xen_configuration.interfaces.interface[0].get_dns2()",
					#"vm.xen_conf.interfaces.switch_id":"metaObj.server.virtual_machines[0].xen_configuration.interfaces.interface[0].get_switch_id()",
					#"vm.xen_conf.interfaces.switch_port":"metaObj.server.virtual_machines[0].xen_configuration.interfaces.interface[0].get_switch_port()"}

					}
		dict2 = dict()
		listt = sorted(conditionMappings.iterkeys())
		#listt.reverse()
		for key in listt:
			dict2[key] = conditionMappings[key]
		return dict2

	@staticmethod
	def getValueFromConfiguration(metaObj,metaObjGetter):
		metaObjPath = "metaObj.server.virtual_machines[0]"
		metaObjConf = eval('metaObj.server.virtual_machines[0].get_virtualization_type()')

		conf = '.' + str(metaObjConf).lower() + '_configuration.'
		value = metaObjPath + conf + metaObjGetter
		return eval(value)

	@staticmethod
	def getVMMemory(metaObj):
		return ControllerMappings.getValueFromConfiguration(metaObj,'get_memory_mb()')
	
	@staticmethod
	def getVMHDMemory(metaObj):
		return ControllerMappings.getValueFromConfiguration(metaObj,'get_hd_size_mb()')

	@staticmethod
	def getNumberOfVMs(metaObj):
		from vt_manager.models import VirtualMachine

		projectUUID = str(metaObj.server.virtual_machines[0].get_project_id())
		return len(VirtualMachine.objects.filter(projectId = projectUUID))		

