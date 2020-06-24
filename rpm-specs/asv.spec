%global srcname asv

%global jquery_version 3.3.1

# Testing using conda requires the network to install packages.
%bcond_with network

Name:           %{srcname}
Version:        0.4.2
Release:        2%{?dist}
Summary:        Airspeed Velocity: A simple Python history benchmarking tool

# Mostly BSD; MIT for extern & www/vendor/*.{css,js}
License:        BSD and MIT
URL:            https://github.com/airspeed-velocity/asv
Source0:        %{pypi_source}
# Not needed upstream.
Patch0001:      0001-Don-t-allow-extension-build-errors-to-be-ignored.patch
# Not wanted upstream: https://github.com/airspeed-velocity/asv/pull/762
Patch0002:      0002-Unbundle-JSON-minify.patch
# Fedora-specific.
Patch0004:      0004-Remove-unnecessary-shebang.patch
# https://github.com/airspeed-velocity/asv/pull/857
Patch0005:      0005-Disable-W3C-mode-in-Chrome-webdriver.patch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(json-minify)
BuildRequires:  python3dist(six) >= 1.4
BuildRequires:  web-assets-devel
BuildRequires:  (js-jquery >= %{jquery_version} with js-jquery < 4)

BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx-bootstrap-theme

%if %{with network}
BuildRequires:  conda
%endif
%ifarch x86_64 i686 aarch64
BuildRequires:  chromedriver
BuildRequires:  chromium
%endif
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  hg
%ifnarch aarch64 %{power64}
BuildRequires:  pypy
%endif
BuildRequires:  python3dist(feedparser)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(python-hglib) >= 1.5
BuildRequires:  python3dist(rpy2)
BuildRequires:  python3dist(scipy)
BuildRequires:  python3dist(selenium)
BuildRequires:  python3dist(virtualenv)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python3-%{srcname}}
Provides:       bundled(python-asizeof) = 5.10
Provides:       bundled(nodejs-blueimp-md5) = 2.10.0
Requires:       bundled(nodejs-flot) = 0.8.3
Provides:       bundled(nodejs-flot-axislabels) = 0.20120405ga0d11e5
Provides:       bundled(nodejs-flot-orderbars) = 0.20100920
Provides:       bundled(nodejs-stupid-table) = 1.0.1

Requires:       python3dist(setuptools)
Requires:       python3dist(six) >= 1.4
Requires:       python3dist(json-minify)
Requires:       (js-jquery >= %{jquery_version} with js-jquery < 4)
Suggests:       conda
Suggests:       python3-virtualenv
Suggests:       python3-hglib >= 1.5
Suggests:       hg
Suggests:       git

# Recommend "all the Pythons", like tox.
Recommends:     python27
Recommends:     python34
Recommends:     python35
Recommends:     python36
Recommends:     python37
Recommends:     python38
Recommends:     python39
Recommends:     pypy
Recommends:     pypy3
Recommends:     python2
Recommends:     python3

%description
Airspeed Velocity (asv) is a tool for benchmarking Python packages over
their lifetime. It is primarily designed to benchmark a single project
over its lifetime using a given suite of benchmarks. The results are
displayed in an interactive web frontend that requires only a basic static
webserver to host.


%package -n %{srcname}-doc
Summary:        asv documentation
%description -n %{srcname}-doc
Documentation for asv


%prep
%autosetup -n %{srcname}-%{version} -p1

# Remove bundled egg-info
rm -rf %{srcname}.egg-info

# Remove useless shebang
sed -i -e '/^#!\//, 1d' asv/extern/asizeof.py


%build
%py3_build

# generate html docs
PYTHONPATH=$(ls -d build/lib*) \
    sphinx-build-3 docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%py3_install

# Unbundle jQuery
pushd %{buildroot}%{python3_sitearch}/asv/www/vendor
rm jquery-%{jquery_version}.min.js
ln -s %{_jsdir}/jquery/3/jquery.min.js jquery-%{jquery_version}.min.js
popd


%check
# Must do this to load from buildroot
rm -rf asv

%ifarch x86_64 aarch64
WEBDRIVER="--webdriver=ChromeHeadless"
%endif
PYTHONPATH=%{buildroot}%{python3_sitearch} PYTHONDONTWRITEBYTECODE=1 \
     pytest-3 -ra $WEBDRIVER


%files -n %{srcname}
%license LICENSE.rst
%doc README.rst
%{_bindir}/asv
%{python3_sitearch}/%{srcname}
%{python3_sitearch}/%{srcname}-%{version}-py*.egg-info


%files -n %{srcname}-doc
%doc html
%license LICENSE.rst


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.2-2
- Rebuilt for Python 3.9

* Sat May 16 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.2-1
- Update to latest version

* Mon May 11 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.1-8
- Loosen up jQuery dependency

* Sun Feb 23 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.1-7
- Re-bundle flot
- Small cleanups to spec

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-4
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.1-2
- Fix tests against latest Chrome webdriver

* Tue Jun 04 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.1-1
- Update to latest version

* Sun May 26 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4-1
- Update to latest version

* Sat Feb 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.1-7
- Rebuild against jQuery 3.3.1

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 07 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.1-5
- Improve testing of web app
- Fix jQuery unbundling

* Wed Dec 05 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.1-4
- Add missing json-minify Requires

* Tue Nov 13 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.1-3
- Mark bundled JS libraries

* Mon Nov 12 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.1-2
- Unbundle json-minify, jQuery, and flot

* Sun Oct 21 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.1-1
- Update to latest version

* Sat Oct 20 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3-1
- Update to latest version

* Sun Nov 19 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.1-1
- Initial package.
