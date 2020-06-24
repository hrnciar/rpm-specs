Name:           csvdiff
Version:        0.3.1
Release:        12%{?dist}
Summary:        Generate a diff between two CSV files on the command-line

License:        BSD
URL:            https://github.com/larsyencken/csvdiff
Source0:        https://files.pythonhosted.org/packages/source/c/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.1

BuildArch:      noarch

BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
BuildRequires:  python3-PyYAML
Requires:       python3-PyYAML
Requires:       python3-jsonschema
Requires:       python3-click
Requires:       python3-libs

%description
Generate a diff between two CSV files on the command-line.

%prep
%autosetup

#Remove shebang
find %{_builddir}/%{name}-%{version} -name '*.py' \
    -exec sed -i '1{\@^#!/usr/bin/env python@d}' {} \;

%build
%py3_build

%install
%py3_install
install -pDm644 %{SOURCE1} %{buildroot}%{_mandir}/man1/csvdiff.1

%check
#%{__python3} setup.py test

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc AUTHORS.rst CONTRIBUTING.rst HISTORY.rst README.rst  
%{_bindir}/*
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}-py?.?.egg-info
%{_mandir}/man1/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-12
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-9
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-5
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 William Moreno <williamjmorenor@gmail.com> - 0.3.1-1
- Update to v0.3.1 

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-7
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 25 2016 William Moreno <williamjmorenor@gmail.com> - 0.3.0-5
- Update Requires

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Sep 11 2015 William Moreno <williamjmorenor@gmail.com> - 0.3.0-2
- Disable %%test

* Fri Sep 11 2015 William Moreno < williamjmorenor@gmail.com> - 0.3.0-1
- Update to v.0.3.0
- Include manpage
- Update python macros

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Feb 02 2015 William José Moreno Reyes <williamjmorenor@gmail.com> - 0.1.0-4
- Fix %%Requires

* Mon Dec 29 2014 William José Moreno Reyes <williamjmorenor@gmail.com> - 0.1.0-3
- Clean Requires and BuildRequires
- Define %%test to 0 

* Sat Dec 27 2014 William Jose Moreno Reyes <williamjmorenor at gmail.com> - 0.1.0-2
- Fix shebang in %%{_bindir}
- Build using Python3

* Sun Dec 7 2014 William José Moreno Reyes <williamjmorenor at gmail.com> - 0.1.0-1
- Inicial packaging
