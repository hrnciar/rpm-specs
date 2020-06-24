Name:           tldr
Version:        0.5
Release:        2%{?dist}
Summary:        Simplified and community-driven man pages

License:        MIT
URL:            https://github.com/tldr-pages/tldr-python-client
Source0:        https://files.pythonhosted.org/packages/source/t/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-colorama 
BuildRequires:  python3-devel
BuildRequires:  python3-pytest-runner
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-six
BuildRequires:  python3-termcolor

Requires:       python3-colorama
Requires:       python3-setuptools
Requires:       python3-six
Requires:       python3-termcolor

%description
A Python command line client for tldr - Simplified and community-driven
man pages http://tldr-pages.github.io/.

%prep
%autosetup -n %{name}-%{version}
# Remove bundled egg-info
rm -rf %{name}.egg-info

%build
%py3_build

%install
%py3_install
sed -i '1s=^#!/usr/bin/\(python\|env python\)[23]\?=#!%{__python3}=' %{buildroot}/%{_bindir}/%{name}.py
sed -i '1{\=^#!/usr/bin/env python=d}' %{buildroot}%{python3_sitelib}/%{name}.py

%check
%{__python3} setup.py test

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}.py
%{python3_sitelib}/%{name}.py
%{python3_sitelib}/__pycache__/*.pyc
%{python3_sitelib}/%{name}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5-2
- Rebuilt for Python 3.9

* Mon Feb 10 2020 Lumír Balhar <lbalhar@redhat.com> - 0.5-1
- Update to 0.5 (#1800511)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.4-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.4-3
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Lumír Balhar <lbalhar@redhat.com> - 0.4.4-1
- New upstream version

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.2-2
- Rebuilt for Python 3.7

* Thu Apr 05 2018 Lumir Balhar <lbalhar@redhat.com> - 0.4.2-1
- New upstream version

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 05 2017 Lumir Balhar <lbalhar@redhat.com> - 0.4.1-1
- Initial package.
