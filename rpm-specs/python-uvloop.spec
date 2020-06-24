%global modname uvloop

Name:           python-%{modname}
Version:        0.14.0
Release:        1%{?dist}
Summary:        Ultra fast implementation of asyncio event loop on top of libuv

License:        MIT or ASL 2.0
URL:            https://github.com/MagicStack/uvloop
Source0:        %{url}/archive/v%{version}/%{modname}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libuv-devel

%global _description \
uvloop is a fast, drop-in replacement of the built-in asyncio event loop.\
uvloop is implemented in Cython and uses libuv under the hood.

%description %{_description}

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-Cython
#BuildRequires:  python3-aiohttp
#BuildRequires:  python3-psutil
#BuildRequires:  python3-pyOpenSSL

%description -n python3-%{modname} %{_description}

%prep
%autosetup -p1 -n %{modname}-%{version}
# always use cython to generate code
sed -i -e "/self.cython_always/s/False/True/" setup.py
# use system libuv
sed -i -e "/self.use_system_libuv/s/False/True/" setup.py
# To be sure, no 3rd-party stuff
rm -vrf vendor/

%build
%py3_build

%install
%py3_install
# https://github.com/MagicStack/uvloop/issues/70
rm -vf %{buildroot}%{python3_sitearch}/%{modname}/_testbase.py
rm -vf %{buildroot}%{python3_sitearch}/%{modname}/__pycache__/_testbase.*

%check
#{__python3} setup.py test

%files -n python3-%{modname}
%license LICENSE-APACHE LICENSE-MIT
%doc README.rst
%{python3_sitearch}/%{modname}-*.egg-info/
%{python3_sitearch}/%{modname}/

%changelog
* Thu Jun 18 2020 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.14.0-1
- Update to 0.14.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.12.2-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.12.2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.12.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 02 14:15:58 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.12.2-1
- Update to 0.12.2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 15 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.2-2
- Include files which were excluded

* Wed Aug 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.2-1
- Update to 0.11.2

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jul 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.0-1
- Update to 0.11.0

* Thu Jun 21 2018 Jerry James <loganjerry@gmail.com> - 0.10.1-1
- Update to 0.10.1 for python 3.7 support (bz 1556279 and 1584458)

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.1-1
- Update to 0.8.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.0-1
- Update to 0.8.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 07 2017 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.7.2-1
- Update to 0.7.2

* Tue Jan 03 2017 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.7.1-1
- Update to 0.7.1

* Sun Jan 01 2017 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.7.0-1
- Initial package
