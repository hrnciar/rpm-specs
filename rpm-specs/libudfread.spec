Name:           libudfread
Version:        1.1.0
Release:        2%{?dist}
Summary:        UDF reader library
License:        LGPLv2+
URL:            https://code.videolan.org/videolan/libudfread
Source0:        https://code.videolan.org/videolan/%{name}/-/archive/%{version}/%{name}-%{version}.tar.bz2

# https://code.videolan.org/videolan/libudfread/-/merge_requests/2.patch
Patch0:         libudfread-1.1.0-drop_ac_prog_libtool.patch

BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool


%description
This library allows reading UDF filesystems, like raw devices and image files.
The library is created and maintained by VideoLAN Project and is used by
projects like VLC and Kodi.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1


%build
autoreconf -vif
%configure --disable-static
%make_build


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%ldconfig_scriptlets


%files
%doc ChangeLog
%license COPYING
%{_libdir}/libudfread.so.0*

%files devel
%{_includedir}/udfread/
%{_libdir}/libudfread.so
%{_libdir}/pkgconfig/udfread.pc


%changelog
* Thu Sep 03 2020 Xavier Bachelot <xavier@bachelot.org> 1.1.0-2
- Don't glob _includedir
- Patch obsolete m4 macro

* Thu Aug 13 2020 Xavier Bachelot <xavier@bachelot.org> 1.1.0-1
- Initial package
