%global pypi_name feedgenerator
%global sum Standalone version of Django's feedgenerator module
%global commit 6b6572cfd3e7f40993204af5aa70aab443a5b63c
%global shortcommit %(c=%{commit}; echo ${c:0:7})


Name:       python-%{pypi_name}
Version:    1.9
Release:    15%{?dist}
Summary:    %{sum}

License:    BSD
URL:        https://github.com/getpelican/%{pypi_name}
Source0:    https://github.com/getpelican/%{pypi_name}/archive/%{commit}/%{pypi_name}-%{shortcommit}.tar.gz

BuildArch:  noarch
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytz}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist six}

%description
FeedGenerator is a standalone version of Django’s feedgenerator module. It has
evolved over time, including an update for Py3K and numerous other
enhancements.

%package -n python3-%{pypi_name}
Summary:        %{sum}
Requires:  %{py3_dist six pytz}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
FeedGenerator is a standalone version of Django’s feedgenerator module. It has
evolved over time, including an update for Py3K and numerous other
enhancements.

%prep
%autosetup -n %{pypi_name}-%{commit}
rm -rf .tox
rm -rf feedgenerator.egg-info
rm -rf feedgenerator/django/utils/six.py

for f in feedgenerator/django/utils/*py;
do
    sed -i -e 's/from . import six/import six/' -e 's/from .six \(import .*$\)/from six \1/'  $f
done

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/*

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.9-14
- Explicitly BR setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.9-13
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 31 2018 Miro Hrončok <mhroncok@redhat.com> - 1.9-7
- Subpackage python2-feedgenerator has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Wed Aug 01 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.9-6
- Include six and pytz as Requires

* Wed Aug 01 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.9-5
- Remove bundled six

* Tue Jul 24 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.9-4
- Use github tar for the time being

* Tue Jul 24 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.9-3
- Cosmetic improvements

* Tue Sep 27 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.9-2
- Update URL
- Update global macro
- Update source url
- Readd tests

* Tue Sep 27 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.9-1
- Initial rpmbuild
