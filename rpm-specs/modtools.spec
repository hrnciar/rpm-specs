Name:          modtools
Version:       0.0.1
Release:       13%{?dist}
Summary:       Utilities for creating and managing modules

License:       GPLv3
Source0:       http://releases.pagure.org/modularity/modularity-tools/modtools-0.0.1-2.tar.gz 
URL:           https://pagure.io/modularity/modularity-tools
BuildArch:     noarch

BuildRequires: python3-devel
Requires:      python3-modulemd
Requires:      python3-dockerfile-parse
Requires:      python3-pdc-client

%description
Modtools now provides tools generating openshift templates
from module Dockerfiles and creating modulemd files
from package names (intended api of module).

%prep
%autosetup
rm -rf %{name}.egg-info

%build
%py3_build

%install
%py3_install
rm -rf %{buildroot}/%{python3_sitelib}/tests
%files
%license LICENSE
%doc README.md
%{_bindir}/modtools
%{python3_sitelib}/modularity/
%{python3_sitelib}/modtools-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.1-13
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.1-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.1-10
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.0.1-6
- Rebuilt for Python 3.7

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 3 2017 Dominika Hodovska <dhodovsk@redhat.com> 0.0.1-4
- add dist tag

* Fri Jul 21 2017 Dominika Hodovska <dhodovsk@redhat.com> 0.0.1-3
- fix directorystructure

* Wed Jul 12 2017 Dominika Hodovska <dhodovsk@redhat.com> 0.0.1-2
- Fix review request

* Fri Jun 30 2017 Dominika Hodovska <dhodovsk@redhat.com> 0.0.1-1
- Initial version
