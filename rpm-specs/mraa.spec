# Nodejs >= 12 is not supported by current versions of SWIG.
%bcond_with nodejs_pkg

%if %{with nodejs_pkg}
%global BUILD_NODEJS ON
%else
%global BUILD_NODEJS OFF
%endif

Name:          mraa
Version:       2.1.0
Release:       3%{?dist}
Summary:       A low level skeleton library for Industrial IO Communication
License:       MIT
URL:           https://projects.eclipse.org/projects/iot.mraa
Source0:       https://github.com/intel-iot-devkit/mraa/archive/v%{version}.tar.gz
# add patch to disable network access (via git) during build
Patch0:        mraa_no-network-access-v%{version}.patch
# fix build on i686
Patch1:        mraa_fix_i686_build-v%{version}.patch
# https://github.com/eclipse/mraa/pull/1012
Patch2:        mraa_include-Declare-gVERSION-global-as-extern-v%{version}.patch

# To quote "Only x86, arm and mock platforms currently supported"
ExcludeArch: %{power64} s390x

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: json-c-devel
%if %{with nodejs_pkg}
BuildRequires: nodejs-devel nodejs-packaging
%endif
BuildRequires: python3-devel python3-setuptools
BuildRequires: swig
BuildRequires: doxygen graphviz sphinx

%if %{without nodejs_pkg}
Obsoletes: nodejs-mraa < %{version}-%{release}
%endif

%description
mraa is a low level skeleton library for Industrial IO Communication and
includes python, java and Node-JS bindings.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.

%package examples
Summary: Development examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-devel = %{version}-%{release}

%description examples
Various mraa development examples for working with the various interfaces.

%package -n python3-mraa
Summary: Python3 bindings
License: GPLv2+
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n python3-mraa
Python3 bindings for Industrial IO.

%if %{with nodejs_pkg}
%package -n nodejs-mraa
Summary: NodeJS package for mraa low-level I/O library
License: GPLv2+
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n nodejs-mraa
NodeJS bindings for Industrial IO.
%endif

%prep
%autosetup -p 1

pushd examples/javascript
sed -i '1i #!/usr/bin/node' AioA0.js Blink-IO.js GPIO_DigitalRead.js \
    GPIO_DigitalWrite.js firmata.js gpio-tool.js initio.js \
    rgblcd.js uart.js
sed -i '1s/env //' *.js
popd
sed -i '1s/env //' examples/python/*.py

%build
%cmake -DBUILDSWIGNODE=%{BUILD_NODEJS} -DCMAKE_INSTALL_PREFIX:PATH=/usr -DCMAKE_SKIP_RPATH=ON -DVERSION:STRING=%{version} .

%make_build
#make_build iio_driver
#make_build mraajs
#make_build npmpkg
#make_build mraa-gpio

%install
%make_install

#Move the examples to the proper location
mkdir -p %{buildroot}%{_libexecdir}/mraa
mv %{buildroot}%{_datarootdir}/mraa/examples/ %{buildroot}%{_libexecdir}/mraa/examples/

#Remove libtool archives.
find %{buildroot} -name '*.la' -delete

#Set some permissions
chmod 0755 %{buildroot}%{_libexecdir}/mraa/examples/c++/*_cpp
%if %{with nodejs_pkg}
chmod 0755 %{buildroot}%{_libexecdir}/mraa/examples/javascript/*.js
%else
rm -fr %{buildroot}%{_libexecdir}/mraa/examples/javascript/
%endif
chmod 0755 %{buildroot}%{_libexecdir}/mraa/examples/python/*.py

chmod 0755 %{buildroot}%{_libexecdir}/mraa/examples/c/aio
chmod 0755 %{buildroot}%{_libexecdir}/mraa/examples/c/gpio
chmod 0755 %{buildroot}%{_libexecdir}/mraa/examples/c/gpio_advanced
chmod 0755 %{buildroot}%{_libexecdir}/mraa/examples/c/hellomraa
chmod 0755 %{buildroot}%{_libexecdir}/mraa/examples/c/i2c_hmc5883l
chmod 0755 %{buildroot}%{_libexecdir}/mraa/examples/c/i2c_mpu6050
chmod 0755 %{buildroot}%{_libexecdir}/mraa/examples/c/iio
chmod 0755 %{buildroot}%{_libexecdir}/mraa/examples/c/led
chmod 0755 %{buildroot}%{_libexecdir}/mraa/examples/c/pwm
chmod 0755 %{buildroot}%{_libexecdir}/mraa/examples/c/spi
chmod 0755 %{buildroot}%{_libexecdir}/mraa/examples/c/uart
chmod 0755 %{buildroot}%{_libexecdir}/mraa/examples/c/uart_advanced
chmod 0755 %{buildroot}%{_libexecdir}/mraa/examples/c/uart_ow

find %{buildroot}%{_libexecdir}/mraa/examples/python -name \*.py -exec chmod -x "{}" \;

%if %{with nodejs_pkg}
chmod 0755 %{buildroot}%{nodejs_sitelib}/mraa/mraa.node

# Symlink nodejs dependencies
%nodejs_symlink_deps
%endif

%ldconfig_scriptlets

%files
%license COPYING
%doc README.md CONTRIBUTING.md
%{_libdir}/lib%{name}.so.*
%{_bindir}/mraa-*

%files devel
%{_includedir}/mraa/
%{_includedir}/mraa.*
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/lib%{name}.so

%files examples
%{_libexecdir}/mraa/

%files -n python3-mraa
%{python3_sitearch}/*

%if %{with nodejs_pkg}
%files -n nodejs-mraa
%{nodejs_sitelib}/mraa
%endif

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-3
- Rebuilt for Python 3.9

* Tue Apr 21 2020 Björn Esser <besser82@fedoraproject.org> - 2.1.0-2
- Rebuild (json-c)

* Wed Apr 15 2020 Björn Esser <besser82@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0
- Disable Nodejs package, as SWIG does not support Nodejs >= 12
- Add patch to fix build on i686

* Mon Apr 13 2020 Björn Esser <besser82@fedoraproject.org> - 2.0.0-8
- Fix build with '-fno-common'

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-6
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Peter Robinson <pbrobinson@fedoraproject.org> 2.0.0-4
- Minor bugfixes

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 10 2018 Peter Robinson <pbrobinson@fedoraproject.org> 2.0.0-2
- Split examples out to a sub package

* Sun Sep  9 2018 Peter Robinson <pbrobinson@fedoraproject.org> 2.0.0-1
- Update to 2.0.0

* Tue Jul 24 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.9.0-3
- Fix example permissions
- Add json-c build dep

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul  1 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.9.0-1
- Update to 1.9.0

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.8.0-4
- Rebuilt for Python 3.7

* Mon Mar 05 2018 Jared Smith <jsmith@fedoraproject.org> - 1.8.0-3
- Add missing BuildRequires on gcc, gcc-c++

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct  2 2017 Peter Robinson <pbrobinson@fedoraproject.org> 1.8.0-1
- Update to 1.8.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Peter Robinson <pbrobinson@fedoraproject.org> 1.7.0-2
- Rebuild for nodejs 8

* Tue May 16 2017 Peter Robinson <pbrobinson@fedoraproject.org> 1.7.0-1
- Update to 1.7.0

* Tue Apr 25 2017 Peter Robinson <pbrobinson@fedoraproject.org> 1.6.1-2
- Review updates

* Fri Apr  7 2017 Peter Robinson <pbrobinson@fedoraproject.org> 1.6.1-1
- Update to 1.6.1

* Mon Jan  9 2017 Peter Robinson <pbrobinson@fedoraproject.org> 1.5.1-2
- Review updates

* Wed Dec  7 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.5.1-1
- Initial package
