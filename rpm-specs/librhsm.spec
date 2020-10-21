Name:           librhsm
Version:        0.0.3
Release:        2%{?dist}
Summary:        Red Hat Subscription Manager library

License:        LGPLv2+
URL:            https://github.com/rpm-software-management/librhsm
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# Patches backported from upstream
Patch0001:      0001-Replace-bool-option-with-int-to-generate-repo-files.patch
Patch0002:      0002-Generate-repofile-for-any-architecture-if-ALL-is-spe.patch
Patch0003:      0003-Enable-repos-when-generating-a-.repo-file-based-on-e.patch
Patch0004:      0004-Append-ctx_baseurl-prefix-to-gpg_url-RhBug-1708628.patch

BuildRequires:  meson >= 0.37.0
BuildRequires:  gcc
BuildRequires:  pkgconfig(glib-2.0) >= 2.44
BuildRequires:  pkgconfig(gobject-2.0) >= 2.44
BuildRequires:  pkgconfig(gio-2.0) >= 2.44
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.2
BuildRequires:  pkgconfig(openssl)

%description
%{summary}.

%package devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc README.md
%{_libdir}/%{name}.so.*

%files devel
%{_libdir}/%{name}.so
%{_includedir}/rhsm/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 08 2020 Stephen Gallagher <sgallagh@redhat.com> - 0.0.3-1
- Initial release
