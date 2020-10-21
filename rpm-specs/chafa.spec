Name:           chafa
Version:        1.2.1
Release:        3%{?dist}
%global sum     Image-to-text converter for terminal
Summary:        %{sum}
License:        LGPLv3+
URL:            https://hpjansson.org/chafa/
Source0:        https://github.com/hpjansson/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  gtk-doc
BuildRequires:  ImageMagick-devel
BuildRequires:  libtool

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}


%description
Chafa is a command-line utility that converts all kinds of images, including
animated image formats like GIFs, into ANSI/Unicode character output that can
be displayed in a terminal.

It is highly configurable, with support for alpha transparency and multiple
color modes and color spaces, combining a range of Unicode characters for
optimal output.


%package libs
Summary:        %{sum} (library)

%description libs
Shared library for %{name}.


%package static
Summary:        %{sum} (static library)

%description static
Static library for %{name}.


%package devel
Summary:        %{sum} (development files)
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}, such as headers.


%package doc
Summary:        %{sum} (documentation)
Recommends:     %{name}-devel

%description doc
Documentation for %{name}, such as headers.


%prep
%autosetup


%build
autoreconf -ivf

# rpath
sed -i -e 's|hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
       -e 's|runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
       -e "s|runpath_var='LD_RUN_PATH'|runpath_var=DIE_RPATH_DIE|g" \
    configure

%configure --disable-rpath
%make_build


%install
%make_install


%files
%doc AUTHORS COPYING.LESSER README* NEWS
%license COPYING.LESSER
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%files libs
%doc AUTHORS
%license COPYING.LESSER
%{_libdir}/lib%{name}.so.0
%{_libdir}/lib%{name}.so.0.1.1

%files static
%doc AUTHORS
%license COPYING.LESSER
%{_libdir}/lib%{name}.a
%{_libdir}/lib%{name}.la

%files devel
%doc AUTHORS
%license COPYING.LESSER
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/lib%{name}.so

%files doc
%doc AUTHORS
%license COPYING.LESSER
%doc %{_datadir}/gtk-doc/html/%{name}


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 27 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-1
- Update to 1.2.1 (#1742491)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 25 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-1
- Update to 1.0.1 (soversion 0.0.0 -> 0.1.1)
- Rebuilt for new ImageMagick 6.9.10 (#1623249)

* Mon Jul 30 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-1
- Initial package

