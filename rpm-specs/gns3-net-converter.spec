Name:           gns3-net-converter
Version:        1.3.0
Release:        15%{?dist}
Summary:        Convert old ini-style GNS3 topologies to v1+ JSON format

License:        GPLv3
URL:            https://pypi.org/project/gns3-net-converter/
Source0:        https://files.pythonhosted.org/packages/source/g/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
Requires: python3-configobj

%description
GNS3 is a graphical network simulator that allows you to design complex network
topologies. You may run simulations or configure devices ranging from simple 
workstations to powerful routers. 

GNS3 Converter is designed to convert old ini-style GNS3 topologies (<=0.8.7)
to the newer version v1+ JSON format for use in GNS3 v1+.

%prep
%autosetup 

%build
%py3_build

%install
%py3_install


%check
# Does not have one


%files 
%license COPYING
%doc README.rst ChangeLog
%{python3_sitelib}/gns3converter
%{python3_sitelib}/gns3_net_converter-*.egg-info
%{_bindir}/gns3-converter


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-15
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Nicolas Chauvet <kwizart@gmail.com> - 1.3.0-13
- Rebuilt

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-11
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-7
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-3
- Rebuild for Python 3.6

* Fri Jul 29 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.3.0-2
- Fix copy-paste issues
- Use pyhosted urls (more clean)

* Tue Jul 05 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.3.0-1
- Initial spec 
