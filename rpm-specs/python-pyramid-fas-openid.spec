%global modname pyramid_fas_openid
%global _description\
pyramid_fas_openid provides a view for the Pyramid framework that acts as\
an OpenID consumer for the Fedora Account System.


Name:               python-pyramid-fas-openid
Version:            0.3.9
Release:            12%{?dist}
Summary:            A view for pyramid that functions as an OpenID consumer

License:            BSD
URL:                https://github.com/fedora-infra/pyramid_fas_openid
Source0:            %{url}/archive/%{version}/%{modname}-%{version}.tar.gz
BuildArch:          noarch

BuildRequires:      python3-devel
BuildRequires:      python3-openid
BuildRequires:      python3-openid-cla
BuildRequires:      python3-openid-teams
BuildRequires:      python3-pyramid
BuildRequires:      python3-setuptools


%description %_description


%package -n python3-pyramid-fas-openid
Summary: %summary
Requires:           python3-pyramid
Requires:           python3-openid
Requires:           python3-openid-teams
Requires:           python3-openid-cla
%{?python_provide:%python_provide python3-pyramid-fas-openid}


%description -n python3-pyramid-fas-openid %_description


%prep
%setup -q -n %{modname}-%{version}

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info


%build
%py3_build


%install
%py3_install


%files -n python3-pyramid-fas-openid
%doc README.txt
%license LICENSE.txt
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-%{version}*


%changelog
* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.9-12
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.9-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.9-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 14 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.3.9-6
- Drop python2-pyramid-fas-openid (#1651173).

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.9-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 12 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.3.9-2
- Require python2-openid instead of python-openid.

* Tue Dec 12 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.3.9-1
- Update to 0.3.9.
- Add support for Python 3.

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.3.8-7
- Python 2 binary package renamed to python2-pyramid-fas-openid
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
