%define _lto_cflags %{nil}

# Commit hash for tagged release
# https://bitbucket.org/widefido/js8call/downloads/?tab=tags
%global commit c5236ed22f06
%global project widefido

Name:           js8call
Version:        2.2.0
Release:        4%{?dist}
Summary:        Amateur Radio message passing using FT8 modulation

License:        GPLv3+
URL:            http://js8call.com/

# Source archive from bitbucket includes project name and commit for directory.
# Use repack.sh to repack the archive.
Source0:        http://files.js8call.com/%{version}/js8call-%{version}.tgz

# Unbundle boost libraries.
Patch0:         js8call-sys_boost.patch
# js8call assumes it's using bundled hamlib and copies and installs binaries to
# new names.
Patch1:         js8call-hamlib.patch
# Fix missing headers exposed by gcc-11
Patch2:         js8call-gcc11.patch

BuildRequires:  cmake%{?rhel:3} gcc gcc-c++ gcc-gfortran tar
BuildRequires:  asciidoc dos2unix rubygem-asciidoctor
BuildRequires:  desktop-file-utils
# Libraries and devel packages
BuildRequires:  boost-devel 
BuildRequires:  fftw-devel
BuildRequires:  pkgconfig(hamlib)
BuildRequires:  libusbx-devel
BuildRequires:  portaudio-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtserialport-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  systemd-devel


%description
JS8Call is software using the JS8 Digital Mode providing weak signal keyboard
to keyboard messaging to Amateur Radio Operators.

JS8Call is an experiment to test the feasibility of a digital mode with the
robustness of FT8, combined with a messaging and network protocol layer for
weak signal communication on HF, using a keyboard messaging style interface. It
is not designed for any specific purpose other than connecting amateur radio
operators who are operating under weak signal conditions. JS8Call is heavily
inspired by WSJT-X, Fldigi, and FSQCall and would not exist without the hard
work and dedication of the many developers in the amateur radio community.


%prep
%autosetup -p1 -c %{name}-%{version}

# remove bundled boost
rm -rf boost

# convert CR + LF to LF
dos2unix *.ui *.rc *.txt

# Don't specify gnu++11 when 14 is the compiler default.
%if 0%{?fedora}
sed -i 's/--std=gnu++11 //' CMakeLists.txt
%endif


%build
# workaround for hamlib check, i.e. for hamlib_LIBRARY_DIRS not to be empty
export PKG_CONFIG_ALLOW_SYSTEM_LIBS=1
%cmake3 -DBoost_NO_SYSTEM_PATHS=FALSE \
        -Dhamlib_STATIC=FALSE

%cmake_build


%install
%cmake_install

# Buttons don't look right with system default style.
desktop-file-edit --set-key=Exec --set-value="js8call --style=fusion" \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

# Remove COPYING so it can be included with %%liecnse
rm -f %{buildroot}%{_datadir}/doc/JS8Call/COPYING
# Remove unneeded install file
rm -f %{buildroot}%{_datadir}/doc/JS8Call/INSTALL*


%files
%license COPYING
%doc %{_datadir}/doc/JS8Call
%{_bindir}/js8*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}_icon.png
%{_datadir}/%{name}/


%changelog
* Wed Oct 14 2020 Jeff Law <law@redhat.com> - 2.2.0-4
- Add missing #include for gcc-11

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Richard Shaw <hobbes1069@gmail.com> - 2.2.0-1
- Update to 2.2.0.

* Tue Mar 31 2020 Richard Shaw <hobbes1069@gmail.com> - 2.1.1-3
- Rebuild for hamlib 4.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 25 2019 Richard Shaw <hobbes1069@gmail.com> - 2.1.1-1
- Update to 2.1.1.

* Sat Dec 07 2019 Richard Shaw <hobbes1069@gmail.com> - 2.0.1-1
- Update to 2.0.1.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Richard Shaw <hobbes1069@gmail.com> - 1.1.0-1
- Update to 1.1.0.

* Tue Apr 02 2019 Richard Shaw <hobbes1069@gmail.com> - 1.0.0-2
- Update spec per review request comments.

* Mon Apr  1 2019 Richard Shaw <hobbes1069@gmail.com> - 1.0.0-1
- Update to 1.0.0.

* Wed Mar 20 2019 Richard Shaw <hobbes1069@gmail.com> - 1.0.0-0.2.rc2
- Add patch to deal with change in fortran iand behavior with version 9.

* Fri Feb 22 2019 Richard Shaw <hobbes1069@gmail.com> - 1.0.0-0.1.rc1
- Update to 1.0.0-rc1.

* Sat Feb 09 2019 Richard Shaw <hobbes1069@gmail.com> - 0.14.1-1
- Update to 0.14.1.

* Fri Feb 08 2019 Richard Shaw <hobbes1069@gmail.com> - 0.14.0-1
- Update to 0.14.0.

* Thu Jan 24 2019 Richard Shaw <hobbes1069@gmail.com> - 0.13.0-1
- Update to 0.13.0.

* Thu Jan 03 2019 Richard Shaw <hobbes1069@gmail.com> - 0.12.0-1
- Update to 0.12.0.

* Wed Dec 19 2018 Richard Shaw <hobbes1069@gmail.com> - 0.11.0-1
- Update to 0.11.0.

* Sun Dec 02 2018 Richard Shaw <hobbes1069@gmail.com> - 0.10.1-1
- Update to 0.10.1.

* Sat Dec 01 2018 Richard Shaw <hobbes1069@gmail.com> - 0.10.0-1
- Update to 0.10.0.

* Fri Nov 16 2018 Richard Shaw <hobbes1069@gmail.com> - 0.9-1
- new version

* Tue Nov 06 2018 Richard Shaw <hobbes1069@gmail.com> - 0.8.3-1
- Update to 0.8.3.

* Sat Nov 03 2018 Richard Shaw <hobbes1069@gmail.com> - 0.8.2-1
- Update to 0.8.2.

* Fri Nov 02 2018 Richard Shaw <hobbes1069@gmail.com> - 0.8.1-1
- Update to 0.8.1.

* Fri Oct 19 2018 Richard Shaw <hobbes1069@gmail.com> - 0.7.5-1
- Update to 0.7.5.

* Thu Oct 11 2018 Richard Shaw <hobbes1069@gmail.com> - 0.7.3-1
- Update to 0.7.3.

* Thu Oct 11 2018 Richard Shaw <hobbes1069@gmail.com> - 0.7.2-2
- Specfile updates for EL 7 build.

* Mon Oct 08 2018 Richard Shaw <hobbes1069@gmail.com> - 0.7.2-1
- Update to 0.7.2.

* Fri Sep 21 2018 Richard Shaw <hobbes1069@gmail.com> - 0.6.4-4
- More fixes to work around incomplete fork of wsjtx.

* Thu Sep 20 2018 Richard Shaw <hobbes1069@gmail.com> - 0.6.4-3
- Update patch to not build/install redundant binaries with wsjtx.

* Mon Sep 17 2018 Richard Shaw <hobbes1069@gmail.com> - 0.6.4-2
- Update patch to not install duplicate binaries with wsjtx and hamlib.
