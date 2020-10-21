%global srcname rebulk

Name:           python-%{srcname}
Version:        2.0.1
Release:        4%{?dist}
Summary:        ReBulk is a python library that performs advanced searches in strings
# Everything licensed as MIT, except:
# rebulk/toposort.py: Apache (v2.0)
# rebulk/test/test_toposort.py: Apache (v2.0)
License:        MIT and ASL 2.0
URL:            https://github.com/Toilal/rebulk
Source:         https://github.com/Toilal/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest-runner
BuildRequires:  python3-six

%global _description\
ReBulk is a python library that performs advanced searches in strings that\
would be hard to implement using re module or String methods only.\
\
It includes some features like Patterns, Match, Rule that allows developers\
to build a custom and complex string matcher using a readable and\
extendable API.

%description %_description

%package -n python3-%{srcname}
Summary:        %summary
%{?python_provide:%python_provide python3-%{srcname}}
Requires:       python3-six

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install
# Remove shebang from Python3 libraries
for lib in `find %{buildroot}%{python3_sitelib} -name "*.py"`; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py*.egg-info

%changelog
* Thu Oct 08 2020 Juan Orti Alcaine <jortialc@redhat.com> - 2.0.1-4
- BR: python3-setuptools

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-2
- Rebuilt for Python 3.9

* Sun May 17 2020 Juan Orti Alcaine <jortialc@redhat.com> - 2.0.1-1
- Version 2.0.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 01 2019 Juan Orti Alcaine <jortialc@redhat.com> - 2.0.0-1
- Version 2.0.0

* Mon Aug 26 2019 Juan Orti Alcaine <jortialc@redhat.com> - 1.0.1-1
- Version 1.0.1
- Tests now pass on Python 3.8, enable them again

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 13 2019 Juan Orti Alcaine <jortialc@redhat.com> - 1.0.0-2
- Disable tests RHBZ#1716519

* Tue Jun 11 2019 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.0.0-1
- Version 1.0.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-7
- Subpackage python2-rebulk has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 29 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.9.0-3
- Simplify Source URL
- Remove shebang from libraries
- Some files licensed as ASL 2.0

* Tue Aug 29 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.9.0-2
- Require python-six

* Mon Aug 28 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.9.0-1
- Initial RPM release
