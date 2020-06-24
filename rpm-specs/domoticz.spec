#global git_short_hash df9de70
#global git_hash df9de7020c4317a484c39f7330e6d1c9ca3d9ec9

Name:		domoticz
Version:	2020.2
Release:	4%{?dist}
Summary:	Open source Home Automation System

License:	GPLv3+ and ASL 2.0 and Boost and BSD and MIT
URL:		http://www.domoticz.com
Source0:	https://github.com/domoticz/domoticz/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
#Source0:	https://github.com/domoticz/domoticz/archive/%%{git_short_hash}.tar.gz#/%%{name}-%%{version}.tar.gz
Source1:	%{name}.service
Source2:	%{name}.conf
# Manually update version reported inside app
Source3:	%{name}-appversion

# Use system tinyxpath (https://github.com/domoticz/domoticz/pull/1759)
Patch1:		%{name}-tinyxpath.patch
# Use system openzwave includes
Patch2:		%{name}-openzwave.patch
# Fix python detection (https://github.com/domoticz/domoticz/pull/1749)
Patch3:		%{name}-python.patch
# Python 3.8 linking fix
Patch4:		%{name}-python38.patch
# _Py_DEC_REFTOTAL macro has been removed from Python 3.9 by:
# https://github.com/python/cpython/commit/49932fec62c616ec88da52642339d83ae719e924
Patch5:		%{name}-python39.patch
# Boost 1.73 support
Patch6:		%{name}-boost.patch

BuildRequires:	boost-devel
BuildRequires:	cereal-devel
BuildRequires:	cmake
BuildRequires:	curl-devel
BuildRequires:	fontpackages-devel
BuildRequires:	gcc-c++
BuildRequires:	git
BuildRequires:	jsoncpp-devel
BuildRequires:	libopenzwave-devel >= 1.6.0
BuildRequires:	libusb-devel
BuildRequires:	lua-devel
BuildRequires:	minizip-compat-devel
BuildRequires:	mosquitto-devel
BuildRequires:	openssl-devel
BuildRequires:	python3-devel
BuildRequires:	sqlite-devel
BuildRequires:	systemd-devel
BuildRequires:	tinyxpath-devel
BuildRequires:	zlib-devel

Requires(pre):	shadow-utils
Requires(post):	systemd
Requires(postun):	systemd
Requires(preun):	systemd

Requires:	google-droid-sans-fonts
Recommends:	system-python-libs >= 3.4

Provides:	bundled(js-ace)
Provides:	bundled(js-angularamd) = 0.2.1
Provides:	bundled(js-angularjs) = 1.5.8
Provides:	bundled(js-blockly)
Provides:	bundled(js-bootbox)
Provides:	bundled(js-bootstrap) = 3.2.0
Provides:	bundled(js-colpick)
Provides:	bundled(js-d3)
Provides:	bundled(js-datatables-datatools) = 2.2.3
Provides:	bundled(js-dateformat) = 1.2.3
Provides:	bundled(js-filesaver) = 0.0-git20140725
Provides:	bundled(js-highcharts) = 4.2.6
Provides:	bundled(js-html5shiv) = 3.6.2
Provides:	bundled(js-i18next) = 1.8.0
Provides:	bundled(js-jquery) = 1.12.0
Provides:	bundled(js-ngdraggable)
Provides:	bundled(js-nggrid)
Provides:	bundled(js-jquery-noty) = 2.1.0
Provides:	bundled(js-require) = 2.1.14
Provides:	bundled(js-respond) = 1.1.0
Provides:	bundled(js-angular-ui-bootstrap) = 0.13.4
Provides:	bundled(js-wow) = 0.1.9
Provides:	bundled(js-ozwcp)
Provides:	bundled(js-less) = 1.3.0
Provides:	bundled(js-ion-sound) = 3.0.6
Provides:	bundled(js-zeroclipboard) = 1.0.4

%global _python_bytecompile_extra 0


%description
Domoticz is a Home Automation System that lets you monitor and configure various
devices like: Lights, Switches, various sensors/meters like Temperature, Rain,
Wind, UV, Electra, Gas, Water and much more. Notifications/Alerts can be sent to
any mobile device


%prep
%setup -q -n %{name}-%{version}
#setup -q -n %{name}-%{git_hash}
%patch1 -p1 -b.tinyxpath
%patch2 -p1 -b.openzwave
%patch3 -p1 -b.python
%if 0%{?fedora} >= 32
%patch4 -p1 -b.python38
%endif
%if 0%{?fedora} >= 33
%patch5 -p1 -b.python39
%patch6 -p1 -b.boost173
%endif
rm -f hardware/openzwave/*.h
rm -rf hardware/openzwave/aes
rm -rf hardware/openzwave/command_classes
rm -rf hardware/openzwave/platform
rm -rf hardware/openzwave/value_classes
rm -rf sqlite/
rm -rf tinyxpath/
cp -p %{SOURCE3} ./appversion.h


%build
%cmake \
 -DCMAKE_BUILD_TYPE=RelWithDebInfo \
 -DUSE_STATIC_LIBSTDCXX=NO \
 -DUSE_STATIC_OPENZWAVE=NO \
 -DUSE_OPENSSL_STATIC=NO \
 -DUSE_BUILTIN_JSONCPP=NO \
 -DUSE_BUILTIN_LUA=NO \
 -DUSE_BUILTIN_MINIZIP=NO \
 -DUSE_BUILTIN_MQTT=NO \
 -DUSE_BUILTIN_SQLITE=NO \
 -DUSE_BUILTIN_TINYXPATH=NO \
 -DUSE_STATIC_BOOST=NO \
 -DCMAKE_INSTALL_PREFIX=%{_datadir}/%{name} \
 .
make %{?_smp_mflags}


%install
%make_install

# remove bundled OpenZWave configuration files so system files are used
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/Config/

# remove docs, we grab them in files below
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/*.txt

# move binary to standard directory
mkdir -p $RPM_BUILD_ROOT%{_bindir}/
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name} $RPM_BUILD_ROOT%{_bindir}/

# install systemd service and config
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/
mkdir -p $RPM_BUILD_ROOT%{_unitdir}/
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}

# create backups/database/plugins/scripts/ssl cert directory
mkdir -p $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/{backups,plugins,scripts}
mkdir -p $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/{dzVents,lua,lua_parsers,python,templates}
mkdir -p $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/dzVents/{data,generated_scripts,scripts}

# Disable the app's self-update script
chmod 644 $RPM_BUILD_ROOT%{_datadir}/%{name}/updatedomo

# Unbundle DroidSans.ttf
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/www/styles/elemental/fonts/DroidSans.ttf
ln -s %{_fontdir}/google-droid/DroidSans.ttf \
      $RPM_BUILD_ROOT%{_datadir}/%{name}/www/styles/elemental/fonts/
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/www/styles/element-light/fonts/DroidSans.ttf
ln -s %{_fontdir}/google-droid/DroidSans.ttf \
      $RPM_BUILD_ROOT%{_datadir}/%{name}/www/styles/element-light/fonts/
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/www/styles/element-dark/fonts/DroidSans.ttf
ln -s %{_fontdir}/google-droid/DroidSans.ttf \
      $RPM_BUILD_ROOT%{_datadir}/%{name}/www/styles/element-dark/fonts/

# Workaround lookup path for dzVents
ln -s %{_datadir}/%{name}/scripts/lua/JSON.lua \
      $RPM_BUILD_ROOT%{_datadir}/%{name}/dzVents/runtime/JSON.lua

# Link default plugins and scripts to userdata directory
ln -s %{_datadir}/%{name}/scripts/dzVents/data/README.md \
      $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/dzVents/data/README.md
ln -s %{_datadir}/%{name}/scripts/dzVents/generated_scripts/README.md \
      $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/dzVents/generated_scripts/README.md
ln -s %{_datadir}/%{name}/scripts/dzVents/scripts/README.md \
      $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/dzVents/scripts/README.md
ln -s %{_datadir}/%{name}/scripts/templates/All.{dzVents,Lua,Python} \
      $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/templates/
ln -s %{_datadir}/%{name}/scripts/templates/Bare.dzVents \
      $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/templates/
ln -s %{_datadir}/%{name}/scripts/templates/Device.{dzVents,Lua} \
      $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/templates/
ln -s %{_datadir}/%{name}/scripts/templates/global_data.dzVents \
      $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/templates/
ln -s %{_datadir}/%{name}/scripts/templates/Group.dzVents \
      $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/templates/
ln -s %{_datadir}/%{name}/scripts/templates/HTTPRequest.dzVents \
      $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/templates/
ln -s %{_datadir}/%{name}/scripts/templates/Scene.dzVents \
      $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/templates/
ln -s %{_datadir}/%{name}/scripts/templates/Security.{dzVents,Lua} \
      $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/templates/
ln -s %{_datadir}/%{name}/scripts/templates/Time.Lua \
      $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/templates/
ln -s %{_datadir}/%{name}/scripts/templates/Timer.dzVents \
      $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/templates/
ln -s %{_datadir}/%{name}/scripts/templates/UserVariable.{dzVents,Lua} \
      $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/templates/

# Byte compile the default plugin
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/%{name}/plugins/AwoxSMP


%pre
getent group domoticz >/dev/null || groupadd -r domoticz
getent passwd domoticz >/dev/null || \
useradd -r -g domoticz -d %{_datadir}/%{name} -s /sbin/nologin \
-c "Domoticz Home Automation Server" domoticz
# For OpenZWave USB access (/dev/ttyACM#)
usermod -G domoticz,dialout domoticz


%post
%systemd_post %{name}.service


%preun
%systemd_preun %{name}.service


%postun
%systemd_postun_with_restart %{name}.service


%files
%license License.txt
%doc README.md History.txt
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_datadir}/%{name}/
%attr(0755,domoticz,domoticz) %{_sharedstatedir}/%{name}/
%{_unitdir}/%{name}.service


%changelog
* Wed Jun 03 2020 Michael Cronenworth <mike@cchtml.com> - 2020.2-4
- Rebuild for Boost 1.73 (RHBZ#1843104)

* Sat May 30 2020 Björn Esser <besser82@fedoraproject.org> - 2020.2-3
- Rebuild (jsoncpp)
- Add a patch to fix build with Python 3.9 (RHBZ#1842068)

* Mon Apr 27 2020 Michael Cronenworth <mike@cchtml.com> - 2020.2-2
- Link against older minizip

* Mon Apr 27 2020 Michael Cronenworth <mike@cchtml.com> - 2020.2-1
- New stable release

* Tue Apr 21 2020 Michael Cronenworth <mike@cchtml.com> - 2020.1-2
- Fix dzVents (RHBZ#1759558)

* Tue Mar 24 2020 Michael Cronenworth <mike@cchtml.com> - 2020.1-1
- New stable release

* Wed Feb 05 2020 Michael Cronenworth <mike@cchtml.com> - 4.11671-0.git20200202.1
- Update git checkout

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.11553-0.git20191207.1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 07 2019 Michael Cronenworth <mike@cchtml.com> - 4.11553-0.git20191207.1
- Update git checkout (RHBZ#1780739)

* Wed Oct 09 2019 Michael Cronenworth <mike@cchtml.com> - 4.11352-0.git20191006.1
- Update git checkout and fix scripts directories (RHBZ#1759558)

* Sat Aug 31 2019 Michael Cronenworth <mike@cchtml.com> - 4.11250-0.git20190831.1
- Fix app version to match upstream versioning
- Fix default userdata location so the app can write to it

* Sat Aug 31 2019 Michael Cronenworth <mike@cchtml.com> - 4.10718-0.git20190831.1
- Version update to current master git checkout
- Compile against OpenZWave 1.6

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.9700-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.9700-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Jonathan Wakely <jwakely@redhat.com> - 4.9700-5
- Rebuilt for Boost 1.69

* Wed Jan 23 2019 Björn Esser <besser82@fedoraproject.org> - 4.9700-4
- Append curdir to CMake invokation. (#1668512)

* Sun Nov 11 2018 Michael Cronenworth <mike@cchtml.com> - 4.9700-3
- Add patch to support Python 3.7

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.9700-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Michael Cronenworth <mike@cchtml.com> - 4.9700-1
- Version update

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.8153-7
- Rebuilt for Python 3.7

* Mon Jun 18 2018 Michael Cronenworth <mike@cchtml.com> - 3.8153-6
- Do not compile some of the extra Python files
- Add patch to fix bug in OZWCP javascript

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.8153-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Michael Cronenworth <mike@cchtml.com> - 3.8153-4
- Add OpenZWave Command Class Barrier support
- Boost 1.66 support (RHBZ#1538585)

* Fri Sep 08 2017 Michael Cronenworth <mike@cchtml.com> - 3.8153-3
- Fix OpenZWave control panel symlink (RHBZ#1482266)
- Fix Python detection

* Mon Jul 31 2017 Michael Cronenworth <mike@cchtml.com> - 3.8153-2
- Fix OpenZWave control panel

* Mon Jul 31 2017 Michael Cronenworth <mike@cchtml.com> - 3.8153-1
- New upstream version
- Unbundle tinyxpath

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5877-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Kalev Lember <klember@redhat.com> - 3.5877-2
- Rebuilt for Boost 1.64

* Wed Jul 19 2017 Michael Cronenworth <mike@cchtml.com> - 3.5877-1
- Initial spec
