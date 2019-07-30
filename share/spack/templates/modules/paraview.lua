{% extends "modules/modulefile.lua" %}
{% block footer %}
{% set paraview_version = 'paraview-{0}'.format(spec.version.up_to(2)) %}
{% set paraview_suffix = '-pv{0}'.format(spec.version.up_to(2)) %}
setenv PARAVIEW_ROOT_DIR "{{ spec.prefix }}"
setenv PARAVIEW_INC_DIR "{{ spec.prefix }}/include/{{ paraview_version }}"
if isDir("{{ spec.prefix }}/lib") then
  setenv PARAVIEW_LIB_DIR "{{ spec.prefix }}/lib/{{ paraview_version }}"
  setenv VTK_DIR "{{ spec.prefix }}/lib/cmake/{{ paraview_version }}"
elseif isDir("{{ spec.prefix }}/lib64") then
  setenv PARAVIEW_LIB_DIR "{{ spec.prefix }}/lib64/{{ paraview_version }}"
  setenv VTK_DIR "{{ spec.prefix }}/lib64/cmake{{ paraview_version }}"
end
setenv PARAVIEW_LIB_SUFFIX "{{ paraview_suffix }}"
setenv PARAVIEW_CATALYST_LIBS " \
  -lvtkCommonExecutionModel{{ paraview_suffix }} \
  -lvtkIOParallelXML{{ paraview_suffix }} \
  -lvtkPVCatalyst{{ paraview_suffix }} \
  -lvtkPVPythonCatalyst{{ paraview_suffix }} \
  -lvtkCommonDataModel{{ paraview_suffix }} \
  -lvtkCommonCore{{ paraview_suffix }} \
  -lvtkParallelCore{{ paraview_suffix }} \
"
{% endblock %}
