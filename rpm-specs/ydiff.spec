Name:       ydiff
Version:    1.1
Release:    9%{?dist}
Summary:    View colored, incremental diff
URL:        https://github.com/ymattw/ydiff
License:    BSD
Source0:    https://github.com/ymattw/ydiff/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires: python3-devel
BuildArch: noarch

Requires: less
Requires: python%{python3_pkgversion}-%{name}
%description
Term based tool to view colored, incremental diff in a Git/Mercurial/Svn
workspace or from stdin, with side by side (similar to diff -y) and auto
pager support.

%package -n     python3-%{name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{name}}
%description -n python3-%{name}
Python library that implements API used by ydiff tool.

%prep
%autosetup -n %{name}-%{version}
/usr/bin/sed -i '/#!\/usr\/bin\/env python/d' ydiff.py

%build
%py3_build

%install
%py3_install

%files
%doc README.rst
%license LICENSE
%{_bindir}/ydiff

%files -n python3-%{name}
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{name}.py
%{python3_sitelib}/%{name}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1-9
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1-6
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1-2
- Rebuilt for Python 3.7

* Thu Jun 28 2018 Alois Mahdal <n9042e84@vornet.cz> 1.1-1
- Initial packaging.
