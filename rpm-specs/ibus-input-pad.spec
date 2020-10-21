Name:       ibus-input-pad
Version:    1.4.99.20140916
Release:    13%{?dist}
Summary:    Input Pad for IBus
License:    GPLv2+
URL:        https://github.com/fujiwarat/input-pad/wiki
Source0:    https://github.com/fujiwarat/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
# Patch0:     %%{name}-HEAD.patch
Patch0:     %{name}-HEAD.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext-devel
BuildRequires:  git
BuildRequires:  gtk3-devel
BuildRequires:  libappstream-glib
BuildRequires:  libtool
BuildRequires:  ibus-devel
BuildRequires:  input-pad-devel
BuildRequires:  intltool
Requires:       ibus

%description
The input pad engine for IBus platform.

%prep
%autosetup -S git

%build
libtoolize -c -f
autoreconf -v -f -i
%configure \
    --disable-static
%make_build

%install
%make_install

# Register as an AppStream component to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_metainfodir}
cat > $RPM_BUILD_ROOT%{_metainfodir}/input-pad.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<component type="inputmethod">
  <id>input-pad.xml</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>Input Pad</name>
  <summary>Input Pad input method</summary>
  <description>
    <p>
      The Input Pad input method is designed for entering special symbols.
    </p>
    <p>
      Input methods are typing systems allowing users to input complex languages.
      They are necessary because these contain too many characters to simply be laid
      out on a traditional keyboard.
    </p>
  </description>
  <url type="homepage">https://github.com/fujiwarat/input-pad/wiki</url>
  <url type="bugtracker">https://github.com/fujiwarat/ibus-input-pad/issues</url>
  <url type="help">https://github.com/fujiwarat/input-pad/wiki/Installation</url>
  <screenshots>
    <screenshot type="default">
      <caption>Input Pad for IBus</caption>
      <image type="source" width="1600" height="900">https://raw.githubusercontent.com/fujiwarat/input-pad/master/web/images/screenshot1.png</image>
    </screenshot>
  </screenshots>
  <update_contact>fujiwara_AT_redhat.com</update_contact>
</component>
EOF

%find_lang %{name}

%check
desktop-file-validate \
    $RPM_BUILD_ROOT%{_datadir}/applications/ibus-setup-input-pad.desktop
appstream-util validate-relax --nonet \
    $RPM_BUILD_ROOT%{_metainfodir}/*.appdata.xml

%post
[ -x %{_bindir}/ibus ] && \
  %{_bindir}/ibus write-cache --system &>/dev/null || :

%postun
[ -x %{_bindir}/ibus ] && \
  %{_bindir}/ibus write-cache --system &>/dev/null || :

%files -f %{name}.lang
%doc AUTHORS README
%license COPYING
%{_libexecdir}/ibus-engine-input-pad
%{_libexecdir}/ibus-setup-input-pad
%{_metainfodir}/*.appdata.xml
%{_datadir}/applications/ibus-setup-input-pad.desktop
%{_datadir}/ibus/component/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.99.20140916-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.99.20140916-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.99.20140916-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.99.20140916-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.99.20140916-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Takao Fujiwara <tfujiwar@redhat.com> - 1.4.99.20140916-8
- Unretire

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.99.20140916-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.99.20140916-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 02 2015 Takao Fujiwara <tfujiwar@redhat.com> - 1.4.99.20140916-5
- Changed URL

* Mon Jul 06 2015 Takao Fujiwara <tfujiwar@redhat.com> - 1.4.99.20140916-4
- Fixed Bug 1239573 - FTBFS

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.99.20140916-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 25 2015 Richard Hughes <rhughes@redhat.com> - 1.4.99.20140916-2
- Register as an AppStream component.

* Tue Sep 16 2014 Takao Fujiwara <tfujiwar@redhat.com> - 1.4.99.20140916-1
- Bumped to 1.4.99.20140916

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Dec 27 2013 Takao Fujiwara <tfujiwar@redhat.com> - 1.4.2-1
- Bumped to 1.4.2

* Fri Dec 06 2013 Takao Fujiwara <tfujiwar@redhat.com> - 1.4.1-1
- Bumped to 1.4.1

* Tue Oct 08 2013 Takao Fujiwara <tfujiwar@redhat.com> - 1.4.0-12
- Added ibus write-cache in %%post and %%postun

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 05 2013 Takao Fujiwara <tfujiwar@redhat.com> - 1.4.0-10
- Added autoreconf to use autoconf 2.69 or later. BZ#925569

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar 06 2012 Takao Fujiwara <tfujiwar@redhat.com> - 1.4.0-7
- Rebuilt for ibus 1.4.99.20120304

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.4.0-5
- Rebuild for new libpng

* Fri Feb 11 2011 Matthias Clasen <mclasen@redhat.com> - 1.4.0-4
- Rebuild against newer gtk

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 18 2011 Takao Fujiwara <tfujiwar@redhat.com> - 1.4.0-2
- Rebuilt for GTK3.

* Fri Dec 03 2010 Takao Fujiwara <tfujiwar@redhat.com> - 1.4.0-1
- Bumped to 1.4.0

* Mon Jul 26 2010 Takao Fujiwara <tfujiwar@redhat.com> - 0.1.3-1
- Bumped to 0.1.3

* Thu Jul 08 2010 Takao Fujiwara <tfujiwar@redhat.com> - 0.1.2-1
- Bumped to 0.1.2
- Added setup dialog.

* Wed Jun 30 2010 Takao Fujiwara <takao.fujiwara1@gmail.com> - 0.1.0.20100630-1
- Initial Implementation. Bug 604500
