%global srcname intervaltree

Name:           python-%{srcname}
Version:        3.0.2
Release:        4%{?dist}
Summary:        A mutable, self-balancing interval tree for Python

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/i/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
A mutable, self-balancing interval tree for Python. Queries may
be by point, by range overlap, or by range envelopment.

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
Requires:       python3-sortedcontainers

%description -n python3-%{srcname}
A mutable, self-balancing interval tree for Python. Queries may
be by point, by range overlap, or by range envelopment.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%{python3_sitelib}/*
%license LICENSE.txt
%doc README.md CHANGELOG.md

%changelog
* Tue Jun 24 2020 W. Michael Petullo <mike@flyn.org> - 3.0.2-4
- BuildRequires setuptools per email "Please BuildRequire python3-setuptools explicitly"

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.2-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 W. Michael Petullo <mike@flyn.org> - 3.0.2-1
- New upstream version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 03 2019 W. Michael Petullo <mike@flyn.org> - 2.1.0-5
- Remove Python 2 subpackage

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-2
- Rebuilt for Python 3.7

* Sat Jun 16 2018 W. Michael Petullo <mike@flyn.org> - 3.12.0-1
- Initial package
