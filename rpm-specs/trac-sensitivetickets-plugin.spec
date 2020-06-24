%if 0%{?rhel} && 0%{?rhel} <= 5
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%define         svn_rev 12442

Name:           trac-sensitivetickets-plugin
Version:        0.21
Release:        15.20121220svn%{?dist}
Summary:        Plugin for Trac that enables sensitive tickets

License:        GPL+
URL:            http://trac-hacks.org/wiki/SensitiveTicketsPlugin
# Generate via 'svn export -r%%{svn_rev} http://trac-hacks.org/svn/sensitiveticketsplugin/trunk trac-sensitivetickets-plugin-0.21 && tar -czvf trac-sensitivetickets-plugin-0.21.svn%%{svn_rev}.tar.gz trac-sensitivetickets-plugin-0.21
Source0:        trac-sensitivetickets-plugin-0.21.svn%{svn_rev}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel, python2-setuptools
Requires:       trac >= 0.11.6

%description
SensitiveTickets is a plugin that lets users mark tickets as "sensitive"
with a checkbox on the ticket form. Sensitive tickets are viewable only 
to those with the SENSITIVE_VIEW permission.

Beware: Hooks that send mail on ticket changes will still send mail for 
sensitive tickets; this may not be what you want.

Beware: if the plugin is removed, disabled, or fails to load, trac will 
opt to display sensitive tickets ("failing open" instead of "failing closed").

%prep
%setup -q


%build
%py2_build

%install
rm -rf $RPM_BUILD_ROOT
%py2_install

%files
# For noarch packages: sitelib
%{python2_sitelib}/*


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-15.20121220svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-14.20121220svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-13.20121220svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-12.20121220svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.21-11.20121220svn
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-10.20121220svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-9.20121220svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-8.20121220svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-7.20121220svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-6.20121220svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-5.20121220svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-4.20121220svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-3.20121220svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 18 2012 Patrick Uiterwijk <puiterwijk@gmail.com> - 0.21-2.20121220svn
- Fixed python2/python3 ambiguity mentioned in RHBZ 887543, comment 1

* Mon Dec 17 2012 Patrick Uiterwijk <puiterwijk@gmail.com> - 0.21-1.20121220svn
- Initial packaging effort

