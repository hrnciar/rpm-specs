%if 0%{?fedora} || 0%{?rhel} >= 8
%global py2pkg_suffix 2
%endif # 0#{?fedora} || 0#{?rhel} >= 8

%global pypi_name jcconv
%global common_desc				\
%{summary} - inter-convert hiragana, katakana,	\
half-width kana.


Name:		python-%{pypi_name}
Version:	0.2.4
Release:	15%{?dist}
Summary:	JapaneseCharacterCONVerter

License:	MIT
URL:		https://pypi.python.org/pypi/%{pypi_name}
Source0:	https://github.com/besser82/jcconv/archive/v%{version}.tar.gz#/%{pypi_name}-%{version}.tar.gz

BuildArch:	noarch

%description
%{common_desc}


%package -n python3-%{pypi_name}
Summary:%{summary}

BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-six

Requires:	python3-six

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{common_desc}


%prep
%autosetup -n %{pypi_name}-%{version}


%build
%py3_build


%install
%py3_install


%check
%{__python3} setup.py test -vv


%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc %{pypi_name}.egg-info/PKG-INFO README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-15
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-13
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-12
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2.4-9
- Subpackage python2-jcconv has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-3
- Rebuild for Python 3.6

* Mon Oct 03 2016 Björn Esser <fedora@besser82.io> - 0.2.4-2
- Add py2pkg_suffix to support epel <= 7

* Mon Oct 03 2016 Björn Esser <fedora@besser82.io> - 0.2.4-1
- Initial import (rhbz 1380671)

* Sat Oct 01 2016 Björn Esser <fedora@besser82.io> - 0.2.4-0.1
- Update to new release

* Fri Sep 30 2016 Björn Esser <fedora@besser82.io> - 0.2.3-0.2
- Add Python 3 support
- Informed upstream of missing license

* Thu Sep 29 2016 Björn Esser <fedora@besser82.io> - 0.2.3-0.1
- Initial package (rhbz 1380671)
