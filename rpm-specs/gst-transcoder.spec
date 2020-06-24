%global apiver 1.0

Name:           gst-transcoder
Version:        1.16.0
Release:        3%{?dist}
Summary:        GStreamer Transcoding API

License:        LGPLv2+
URL:            https://github.com/pitivi/gst-transcoder
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  gobject-introspection-devel
#BuildRequires:  gtk-doc

%description
%{summary}.

%package devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
# https://github.com/pitivi/gst-transcoder/issues/4
Requires:       gstreamer1-devel%{?_isa}

%description devel
%{summary}.

%prep
%autosetup

%build
%meson -D disable_doc=true
%meson_build

%install
%meson_install

%ldconfig_scriptlets

%files
%license LICENSE
%{_bindir}/%{name}-%{apiver}
%dir %{_libdir}/girepository-1.0/
%{_libdir}/girepository-1.0/GstTranscoder-%{apiver}.typelib
%{_libdir}/gstreamer-1.0/libgsttranscode.so
%{_libdir}/libgsttranscoder-%{apiver}.so.*
%{_datadir}/gstreamer-1.0/encoding-profiles/

%files devel
%{_includedir}/gstreamer-1.0/gst/transcoder/
%{_libdir}/libgsttranscoder-%{apiver}.so
%{_libdir}/pkgconfig/%{name}-%{apiver}.pc
%dir %{_datadir}/gir-1.0/
%{_datadir}/gir-1.0/GstTranscoder-%{apiver}.gir
#%dir %{_datadir}/gtk-doc
#%dir %{_datadir}/gtk-doc/html
#%{_datadir}/gtk-doc/html/gstreamer-transcoder/

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 20 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.16.0-1
- 1.16.0

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 1.15.90-2
- Rebuild with Meson fix for #1699099

* Mon Apr 15 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.15.90-1
- 1.15.90

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 27 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.14.0-1
- 1.14.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 25 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.12.1-1
- 1.12.1, BZ 1494760.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.12.1-1
- Update to 1.12.1

* Thu Jun 22 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.12.0-1
- 1.12.0, BZ 1463448.
- Disabled gtk-doc to resolve circular BR.

* Fri Apr 07 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.11.1-3
- Add BR for gtk-doc to fix FTBFS, BZ 1423696

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 25 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.11.1-1
- Update to 1.11.1 (RHBZ #1416395)

* Tue Dec 13 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.8.2-2
- Use proper macro for building to not ignore CFLAGS and cetera
- Update summary/description
- Move gir under devel subpackage
- Other trivial fixes

* Mon Aug 08 2016 Jon Ciesla <limburgher@gmail.com> - 1.8.2-1
- 1.8.2

* Thu Jul 14 2016 Jon Ciesla <limburgher@gmail.com> - 1.8.1-1
- 1.8.1

* Thu Jul 14 2016 Jon Ciesla <limburgher@gmail.com> - 1.8.0-4
- Use %%{name} macro, tab/space fixes.

* Wed Jul 13 2016 Jon Ciesla <limburgher@gmail.com> - 1.8.0-3
- Add isa Requires, fix several macros

* Mon Jul 11 2016 Jon Ciesla <limburgher@gmail.com> - 1.8.0-2
- Fix directory ownership.

* Fri Jul 01 2016 Jon Ciesla <limburgher@gmail.com> - 1.8.0-1
- First build.
