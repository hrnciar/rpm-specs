Name:           libgit2_0.28
Version:        0.28.5
Release:        2%{?dist}
Summary:        C implementation of the Git core methods as a library with a solid API
License:        GPLv2 with exceptions
URL:            https://libgit2.org/
Source0:        https://github.com/libgit2/libgit2/archive/v%{version}/libgit2-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  cmake >= 2.8.11
BuildRequires:  ninja-build
BuildRequires:  http-parser-devel
BuildRequires:  libcurl-devel
BuildRequires:  libssh2-devel
BuildRequires:  openssl-devel
BuildRequires:  python3
BuildRequires:  zlib-devel
Provides:       bundled(libxdiff)

%description
libgit2 is a portable, pure C implementation of the Git core methods
provided as a re-entrant linkable library with a solid API, allowing
you to write native speed custom Git applications in any language
with bindings.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
# These devel packages are not installable in parallel
Conflicts:      pkgconfig(libgit2)

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n libgit2-%{version}

# Remove VCS files from examples
find examples -name ".gitignore" -delete -print

# Don't run "online" tests
sed -i '/ADD_TEST(online/s/^/#/' tests/CMakeLists.txt

# Remove bundled libraries
rm -frv deps

%build
%cmake . -B%{_target_platform} \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DSHA1_BACKEND=OpenSSL \
  -DUSE_HTTPS=OpenSSL \
  %{nil}
%ninja_build -C %{_target_platform}

%install
%ninja_install -C %{_target_platform}

%check
%ninja_test -C %{_target_platform}

%files
%license COPYING
%{_libdir}/libgit2.so.*

%files devel
%doc AUTHORS docs examples README.md
%{_libdir}/libgit2.so
%{_libdir}/pkgconfig/libgit2.pc
%{_includedir}/git2.h
%{_includedir}/git2/

%changelog
* Wed Apr 15 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.28.5-2
- Rebuild for http-parser 2.9.4

* Wed Apr 15 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.28.5-1
- Update to 0.28.5

* Tue Mar 03 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.28.4-1
- Initial package
