Name:           cantoolz
Version:        3.7.0
Release:        6%{?dist}
Summary:        A framework for Controller Area Network (CAN) bus analysis

License:        ASL 2.0
URL:            https://github.com/CANToolz/CANToolz
Source0:        https://github.com/CANToolz/CANToolz/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%description
CANToolz is a framework for analyzing CAN networks and devices. It provides
multiple modules that can be chained using CANToolz's pipe system and used by
security researchers, automotive/OEM security testers in black-box analysis.

CANToolz can be used for ECU discovery, MitM testing, fuzzing, brute-forcing,
scanning or R&D, testing and validation.

%prep
%autosetup -n CANToolz-%{version}

%build
%py3_build

%install
%py3_install

# Tests are writing results to files
#%check
#%{__python3} setup.py test

%files
%doc CONTRIBUTORS.md README.md NOTICE.md
%license LICENSE.md
%{_bindir}/%{name}
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/%{name}/
%exclude %{python3_sitelib}/tests/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.7.0-6
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.7.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.7.0-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Fabian Affolter <mail@fabian-affolter.ch> - 3.7.0-1
- Initial package for Fedora
