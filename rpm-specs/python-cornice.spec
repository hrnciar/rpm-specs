%global module cornice
%global desc Helpers to build & document Web Services with Pyramid.

Name:             python-cornice
Version:          4.0.1
Release:          3%{?dist}
BuildArch:        noarch

License:          MPLv2.0
Summary:          Define Web Services in Pyramid
URL:              https://pypi.python.org/pypi/cornice
Source0:          https://github.com/Cornices/cornice/archive/%{version}/%{module}-%{version}.tar.gz


BuildRequires: %{py3_dist colander}
BuildRequires: %{py3_dist coverage}
BuildRequires: %{py3_dist mock}
BuildRequires: %{py3_dist nose}
BuildRequires: %{py3_dist pyramid} >= 1.7
BuildRequires: %{py3_dist setuptools}
BuildRequires: %{py3_dist simplejson}
BuildRequires: %{py3_dist sphinx}
BuildRequires: %{py3_dist venusian}
BuildRequires: %{py3_dist webtest}
BuildRequires: python3-devel


%description
%{desc}


%package -n python3-cornice
Summary:          %{summary}

Recommends: %{py3_dist colander}
Requires:   %{py3_dist pyramid} >= 1.7
Requires:   %{py3_dist simplejson}
Requires:   %{py3_dist six}
Requires:   %{py3_dist venusian}

%{?python_provide:%python_provide python3-%{module}}


%description -n python3-cornice
%{desc}


%prep
%autosetup -p1 -n %{module}-%{version}


%build
%py3_build


%install
%py3_install


%check
PYTHONPATH="." nosetests-3


%files -n python3-cornice
%license LICENSE
%doc CHANGES.txt CONTRIBUTORS.txt README.rst
%{python3_sitelib}/%{module}*


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0.1-2
- Rebuilt for Python 3.9

* Wed Feb 19 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 4.0.1-1
- Update to 4.0.1 (#1778705).
- https://github.com/Cornices/cornice/blob/4.0.1/CHANGES.txt

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 18 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.6.1-1
- Update to 3.6.1 (#1771947).
- https://github.com/Cornices/cornice/blob/3.6.1/CHANGES.txt

* Tue Sep 03 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.6.0-1
- Update to 3.6.0 (#1742282).
- https://github.com/Cornices/cornice/blob/3.6.0/CHANGES.txt

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.5.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 26 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.5.1-1
- Update to 3.5.1 (#1669103).
- https://github.com/Cornices/cornice/blob/3.5.1/CHANGES.txt

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 08 2018 Miro Hrončok <mhroncok@redhat.com> - 3.4.0-2
- Subpackage python2-cornice has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Aug 23 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.4.0-1
- Update to 3.4.0 (#1543660).
- https://github.com/Cornices/cornice/blob/3.4.0/CHANGES.txt

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-2
- Rebuilt for Python 3.7

* Fri Apr 27 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.1.0-1
- Update to 3.1.0.
- https://github.com/Cornices/cornice/blob/3.1.0/CHANGES.txt

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
