%global modname %(n=%{name}; echo ${n//-/_})

Name:           git-archive-all
Version:        1.17.1
Release:        9%{?dist}
Summary:        Archive git repository with its submodules

License:        MIT
URL:            https://github.com/Kentzo/git-archive-all
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# git-submodule is in git, not in git-core
Requires:       git

BuildArch:      noarch

%description
%{summary}.

%prep
%autosetup
#sed -i -e '1{\@^#! /usr/bin/env python@d}' %{modname}.py

%build
%py3_build

%install
%py3_install

%files
%license LICENSE.txt
%doc README.rst
%{_bindir}/%{name}
%{python3_sitelib}/%{modname}-*.egg-info/
%{python3_sitelib}/%{modname}.py
%{python3_sitelib}/__pycache__/%{modname}.*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.17.1-9
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.17.1-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.17.1-6
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.17.1-2
- Rebuilt for Python 3.7

* Thu Feb 22 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.17.1-1
- Update to 1.17.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.16.4-1
- Update to 1.16.4

* Sat Mar 11 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.16-1
- Update to 1.16 (RHBZ #1428620)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Miro Hrončok <mhroncok@redhat.com> - 1.15-2
- Rebuild for Python 3.6

* Tue Dec 13 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.15-1
- Initial package
