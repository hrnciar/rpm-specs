%global qt_module qtspeech

Summary: Qt5 - Speech component
Name:    qt5-%{qt_module}
Version: 5.14.2
Release: 1%{?dist}

# See LGPL_EXCEPTIONS.txt, LICENSE.GPL3, respectively, for exception details
License: LGPLv2 with exceptions or GPLv3 with exceptions
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz

## downstream patches
# workaround https://bugzilla.redhat.com/show_bug.cgi?id=1538715
#Patch100: qtspeech-speech-dispatcher_includes.patch

BuildRequires: qt5-qtbase-devel >= %{version}
BuildRequires: speech-dispatcher-devel >= 0.8

BuildRequires: qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}

Recommends: %{name}-speechd%{?_isa} = %{version}-%{release}

%description
The module enables a Qt application to support accessibility features such as text-to-speech, which is useful for end-users who are
visually challenged or cannot access the application for whatever reason. The most common use case where text-to-speech comes in handy
is when the end-user is driving and cannot attend the incoming messages on the phone. In such a scenario, the messaging application
can read out the incoming message. Qt Serial Port provides the basic functionality, which includes configuring, I/O operations,
getting and setting the control signals of the RS-232 pinouts.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt5-qtbase-devel%{?_isa}
%description devel
%{summary}.

%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
%{summary}.

%package speechd
Summary: %{name} speech-dispatcher plugin
Requires: %{name}%{?_isa} = %{version}-%{release}
%description speechd
%{summary}.


%prep
%setup -q -n %{qt_module}-everywhere-src-%{version}

#patch100 -p1 -b .includes


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{qmake_qt5} .. \
  %{?_qt5_examplesdir:CONFIG+=qt_example_installs}

%make_build


%install
make install INSTALL_ROOT=%{buildroot} -C %{_target_platform}

## .prl/.la file love
# nuke .prl reference(s) to %%buildroot, excessive (.la-like) libs
pushd %{buildroot}%{_qt5_libdir}
for prl_file in libQt5*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd


%ldconfig_scriptlets

%files
%license LICENSE.*
%{_qt5_libdir}/libQt5TextToSpeech.so.5*
%dir %{_qt5_plugindir}/texttospeech/
%dir %{_qt5_libdir}/cmake/Qt5TextToSpeech/

%files speechd
%{_qt5_plugindir}/texttospeech/libqtexttospeech_speechd.so
%{_qt5_libdir}/cmake/Qt5TextToSpeech/Qt5TextToSpeech_QTextToSpeechPluginSpeechd.cmake

%files devel
%{_qt5_headerdir}/QtTextToSpeech/
%{_qt5_libdir}/libQt5TextToSpeech.so
%{_qt5_libdir}/libQt5TextToSpeech.prl
%{_qt5_libdir}/cmake/Qt5TextToSpeech/Qt5TextToSpeechConfig*.cmake
%{_qt5_libdir}/pkgconfig/Qt5TextToSpeech.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_texttospeech*.pri

%files examples
%license LICENSE.FDL
%{_qt5_examplesdir}/


%changelog
* Sat Apr 04 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.14.2-1
- 5.14.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 5.13.2-1
- 5.13.2

* Tue Sep 24 2019 Jan Grulich <jgrulich@redhat.com> - 5.12.5-1
- 5.12.5

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.12.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 14 2019 Jan Grulich <jgrulich@redhat.com> - 5.12.4-1
- 5.12.4

* Tue Jun 04 2019 Jan Grulich <jgrulich@redhat.com> - 5.12.3-1
- 5.12.3

* Fri Feb 15 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.12.1-1
- 5.12.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 07 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.11.3-1
- 5.11.3

* Fri Sep 21 2018 Jan Grulich <jgrulich@redhat.com> - 5.11.2-1
- 5.11.2

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.11.1-1
- 5.11.1

* Sun May 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.11.0-1
- 5.11.0
- use %%make_build %%ldconfig_scriptlets

* Tue Feb 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.10.1-2
- -speechd subpkg, Recommends: -speechd

* Wed Feb 14 2018 Jan Grulich <jgrulich@redhat.com> - 5.10.1-1
- 5.10.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.10.0-2
- enable speech-dispatcher support, workaround bug #1538715

* Wed Dec 20 2017 Jan Grulich <jgrulich@redhat.com> - 5.10.0-1
- 5.10.0

* Sun Nov 26 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.9.3-1
- 5.9.3

* Thu Nov 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.9.2-1
- 5.9.2

* Wed May 24 2017 Helio Chissini de Castro <helio@kde.org> - 5.9.0-0.rc.1
- Upstream Release Candidate 1
