Name:           marshalparser
Version:        0.2.1
Release:        1%{?dist}
Summary:        Parser for Python internal Marshal format

License:        MIT
URL:            https://github.com/fedora-python/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

# For tests on various pyc files
BuildRequires:  python3.6
BuildRequires:  python3.7
BuildRequires:  python3.8
BuildRequires:  python3.9

%generate_buildrequires
%pyproject_buildrequires -t

%description
Parser for Python internal Marshal format which can fix pyc files
reproducibility.

%prep
%autosetup

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name}

%check
%tox

%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
* Wed Sep 16 2020 Lumír Balhar <lbalhar@redhat.com> - 0.2.1-1
- Update to 0.2.1

* Wed Jul 29 2020 Lumír Balhar <lbalhar@redhat.com> - 0.2.0-1
- Update to 0.2.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Lumír Balhar <lbalhar@redhat.com> - 0.1.1-1
- Initial package
