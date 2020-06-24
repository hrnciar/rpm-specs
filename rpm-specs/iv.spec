# Issues filed:
# https://github.com/neuronsimulator/iv/issues/14: -Wstrict-aliasing
# https://github.com/neuronsimulator/iv/issues/15: -Wchar-subscript


%global commit 08c48bbb85434a2fc34cdd483a47c2deae7a289a
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global checkout_date 20191117

Name:           iv
Version:        0
Release:        0.2.%{checkout_date}git%{shortcommit}%{?dist}
Summary:        InterViews graphical library

License:  MIT
URl:      https://github.com/neuronsimulator/%{name}
Source0:  https://github.com/neuronsimulator/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  /usr/bin/aclocal
BuildRequires:  /usr/bin/autoheader
BuildRequires:  /usr/bin/autoconf
BuildRequires:  /usr/bin/libtoolize
BuildRequires:  gcc-c++
BuildRequires:  xorg-x11-server-devel
BuildRequires:  libXext-devel
# Is built against a bundled version, does not provide its libraries etc.
# https://github.com/neuronsimulator/iv/issues/3
Provides: bundled(libtiff) = 3.00

# for %%{_datadir}/X11/app-defaults
Requires: libXt

%description
The InterViews graphical library used by NEURON.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{commit}

# Remove spurious executable permission
chmod -x README Copyright


%build
./build.sh
export X_LIBS="-lX11 -lXext"
%configure --disable-static
%make_build


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -delete

# Don't install these, we don't want anyone using them
rm -vrf $RPM_BUILD_ROOT/%{_includedir}/TIFF

# Move file to right folder
install -pm 0755 -d $RPM_BUILD_ROOT/%{_datadir}/X11/
mv -v $RPM_BUILD_ROOT/%{_datadir}/app-defaults  $RPM_BUILD_ROOT/%{_datadir}/X11/

%files
%license Copyright
%doc README
%{_libdir}/libIVhines.so.3.0.3
%{_libdir}/libIVhines.so.3
%{_libdir}/libUnidrawhines.so.3.0.3
%{_libdir}/libUnidrawhines.so.3
%{_bindir}/idemo
%{_bindir}/iclass
%{_bindir}/idraw
%{_datadir}/X11/app-defaults/

%files devel
%{_includedir}/ivstrm.h
%{_includedir}/ivstream.h
%{_includedir}/ivversion.h
%{_includedir}/Dispatch/
%{_includedir}/OS/
%{_includedir}/IV-2_6/
%{_includedir}/IV-X11/
%{_includedir}/IV-look/
%{_includedir}/InterViews/
%{_libdir}/libIVhines.so
%{_libdir}/libUnidrawhines.so

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20191117git08c48bb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 17 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0-0.1.20191117git08c48bb
- Update as per review comments
- Update to latest upstream commit: fixes -Wsequence-point
- Update to latest upstream commit: fixes library dependencies
- Correct location of app-info file and add Requires
- Improve find command
- Remove license from devel
- File compilation warning issues and note them as comments

* Wed Nov 06 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0-0.0.20191106git74f1207
- Initial rpm build
