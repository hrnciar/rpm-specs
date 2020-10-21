# Created by pyp2rpm-3.2.2
%global pypi_name python-bitcoinlib
%global srcname bitcoinlib

Name:           python-%{srcname}
Version:        0.11.0
Release:        3%{?dist}
Summary:        The Swiss Army Knife of the Bitcoin protocol

License:        LGPLv3+
URL:            https://github.com/petertodd/python-bitcoinlib
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description
This Python 2/3 library provides an easy interface to the bitcoin data
structures and protocol. The approach is lowlevel and "ground up", with
a focus on providing tools to manipulate the internals of how Bitcoin works.

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
This Python 3 library provides an easy interface to the bitcoin data
structures and protocol. The approach is lowlevel and "ground up", with
a focus on providing tools to manipulate the internals of how Bitcoin works.


%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files bitcoin

%check
%{__python3} -m unittest discover

%files -n python3-%{srcname} -f %pyproject_files
%license LICENSE
%doc README.md

%changelog
* Tue Sep 15 2020 Charalampos Stratakis <cstratak@redhat.com> - 0.11.0-3
- Update the package to use pyproject macros

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 01 2020 Charalampos Stratakis <cstratak@redhat.com> - 0.11.0-1
- Update to 0.11.0 (#1811230)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.10.2-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 10 2019 Charalampos Stratakis <cstratak@redhat.com> - 0.10.2-1
- Update to 0.10.2

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10.1-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.10.1-2
- Rebuilt for Python 3.7

* Sat Apr 14 2018 Stratakis Charalampos <cstratak@redhat.com> - 0.10.1-1
- Initial package.