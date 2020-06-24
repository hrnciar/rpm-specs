
%global modname tablib

Name:             python-tablib
Version:          0.12.1
Release:          14%{?dist}
Summary:          Format agnostic tabular data library (XLS, JSON, YAML, CSV)

License:          MIT
URL:              http://github.com/kennethreitz/tablib
Source0:          https://files.pythonhosted.org/packages/source/t/tablib/%{modname}-%{version}.tar.gz
# FIXME(hguemar): fix compat with openpyxl 2.5.x from upstream PR #296
# https://github.com/kennethreitz/tablib/pull/296
Patch001:         fix-openpyxl-2.5.x-compat-pr-296.patch
BuildArch:        noarch

BuildRequires:    /usr/bin/2to3

BuildRequires: python3-pytest
BuildRequires: python3-unicodecsv
BuildRequires: python3-openpyxl
BuildRequires: python3-odfpy
BuildRequires: python3-xlrd
BuildRequires: python3-xlwt
BuildRequires: python3-PyYAML
BuildRequires: python3-pandas

%global _description\
Tablib is a format-agnostic tabular dataset library, written in Python.\
\
Output formats supported:\
\
 - Excel (Sets + Books)\
 - JSON (Sets + Books)\
 - YAML (Sets + Books)\
 - HTML (Sets)\
 - TSV (Sets)\
 - CSV (Sets)

%description %_description

%package -n python3-tablib
Summary:        Format agnostic tabular data library (XLS, JSON, YAML, CSV)

BuildRequires:    python3-devel
BuildRequires:    python3-setuptools
Requires: python3-PyYAML
Requires: python3-unicodecsv
Requires: python3-openpyxl
Requires: python3-odfpy
Requires: python3-xlrd
Requires: python3-xlwt

%description -n python3-tablib
Tablib is a format-agnostic tabular dataset library, written in Python.

Output formats supported:

 - Excel (Sets + Books)
 - JSON (Sets + Books)
 - YAML (Sets + Books)
 - HTML (Sets)
 - TSV (Sets)
 - CSV (Sets)


%prep
%setup -q -n %{modname}-%{version}
%patch001 -p1
# Remove shebangs
for lib in $(find . -name "*.py"); do
 sed '/\/usr\/bin\/env/d' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

sed -i "/\(xlwt\|odf\|xlrd\|openpyxl\|openpyxl\..*\|yaml\)'/d" setup.py
find . -name "*.py" | grep -v 3 | xargs 2to3 -w

sed -i '/tablib.packages.*3/d' setup.py


%build

%{__python3} setup.py build

%install
%{__python3} setup.py install -O1 --skip-build --root=%{buildroot}
 
%check
%{__python3} -m pytest test_tablib.py

%files -n python3-%{modname}
%license
%doc README.rst AUTHORS
%{python3_sitelib}/%{modname}
%{python3_sitelib}/*.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.12.1-14
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.12.1-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.12.1-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 04 2019 Miro Hrončok <mhroncok@redhat.com> - 0.12.1-8
- Subpackage python2-tablib has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul  4 2018 Haïkel Guémar <hguemar@fedoraproject.org> - 0.12.1-6
- Fix compatibility with openpyxl 2.5.x

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.12.1-5
- Rebuilt for Python 3.7

* Mon Mar 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.12.1-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Oct 20 2017 Kevin Fenzi <kevin@scrye.com> - 0.12.1-2
- Change BuildRequires for older PyYAML packages. 

* Wed Oct 11 2017 Kevin Fenzi <kevin@scrye.com> - 0.12.1-1
- Update to 0.12.1.
- Fix requires for no longer bundled items. Fixes bug #1499306
- Enable tests. 

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.11.5-3
- Python 2 binary package renamed to python2-tablib
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Ralph Bean <rbean@redhat.com> - 0.11.5-1
- new version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 20 2016 Tomas Orsava <torsava@redhat.com> - 0.10.0-6
- Added a patch for Python 3.6 compatibility
- Updated PyPI download URL

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.10.0-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Aug 05 2015 Haïkel Guémar <hguemar@fedoraproject.org> - 0.10.0-1
- Upstream 0.10.0
- Enable python3 subpackage

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.11.20120702git752443f-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.11.20120702git752443f-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.11.20120702git752443f-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.11.20120702git752443f-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.11.20120702git752443f-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jul 06 2012 Ralph Bean <rbean@redhat.com> - 0.9.11.20120702git752443f-5
- Disable python3 for now since the package is so unstable.

* Fri Jul 06 2012 Ralph Bean <rbean@redhat.com> - 0.9.11.20120702git752443f-4
- Patch to fix broken setup.py

* Wed Jul 04 2012 Ralph Bean <rbean@redhat.com> - 0.9.11.20120702git752443f-3
- Removed shebangs.

* Wed Jul 04 2012 Ralph Bean <rbean@redhat.com> - 0.9.11.20120702git752443f-2
- Added link to upstream bug for patch.

* Thu Jun 28 2012 Ralph Bean <rbean@redhat.com> - 0.9.11.20120702git752443f-1
- Initial package for Fedora
