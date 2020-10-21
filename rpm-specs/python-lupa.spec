%global srcname lupa
%global commit 831599a4f7333626d336c2ac77968877b2655ab2
%global shortcommit 831599a
%global snapinfo 20200822git%{shortcommit}

%global _description\
Lupa integrates the run-times of Lua or LuaJIT2 into CPython. It is a\
partial rewrite of LunaticPython in Cython with some additional features\
such as proper co-routine support.

Name:		python-%{srcname}
Version:	1.9
Release:	1.%{snapinfo}%{?dist}
Summary:	Python wrapper around Lua and LuaJIT

License:	MIT
URL:		https://pypi.python.org/pypi/lupa
#Source0:	https://github.com/scoder/{srcname}/archive/{srcname}-{version}/{srcname}-{srcname}-{version}.tar.gz
# Lua 5.4 support
Source0:    https://github.com/scoder/%{srcname}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz

BuildRequires: gcc
BuildRequires: lua-devel

%description %_description

%package -n python3-%{srcname}
Summary:	%{summary}
BuildRequires:	python3-devel
BuildRequires:	python3-Cython
BuildRequires:	python3-setuptools
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description


%prep
#autosetup -n {srcname}-{srcname}-{version}
%autosetup -n %{srcname}-%{commit}


%build
%py3_build


%install
%py3_install


%check
%python3 setup.py test


%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.rst CHANGES.rst INSTALL.rst
%{python3_sitearch}/%{srcname}/
%{python3_sitearch}/%{srcname}-*.egg-info


%changelog
* Tue Sep  8 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.9-1.20200820git831599a
- Update to 1.9 post-release snapshot with Lua 5.4 support
- Enable tests

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-13
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.6-11
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.6-5
- Subpackage python2-lupa has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.6-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 01 2018 Dhanesh B. Sabane <dhanesh95@fedoraproject.org> - 1.6-1
- Initial release

