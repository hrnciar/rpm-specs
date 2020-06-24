Name:       bcal
Version:    2.2
Release:    2%{?dist}
Summary:    Storage conversion and expression calculator

License:    GPLv3+
URL:        https://github.com/jarun/bcal
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# Only available for 64bits system
ExclusiveArch: x86_64 aarch64 ia64 ppc64 ppc64le s390x

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  readline-devel

%description
bcal (Byte CALculator) is a command-line utility for storage conversions
and calculations. Storage, hardware and firmware developers work
with numerical calculations regularly e.g., storage unit conversions,
address calculations etc. If you are one and can't calculate the hex address
offset for (512 - 16) MiB immediately, or the value when the 43rd bit of
a 64-bit address is set, bcal is for you

%prep
%autosetup -p1 -n %{name}-%{version}
sed -i '/STRIP ?= strip/d;s/install: bcal/install: /;s/$(CFLAGS)/$(CFLAGS) $(LDFLAGS)/' Makefile

%build
export CFLAGS="-fPIC %{optflags}"
export LDFLAGS="%{?__global_ldflags}"
%make_build bcal

%install
%make_install PREFIX=%{_prefix}

%files
%doc CHANGELOG README.md
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 11 18:02:21 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2.2-1
- Update to 2.2 (#1788743)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.1-4
- Fix bug related to GCC 9.0

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1-3
- Rebuild for readline 8.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 2.1-1
- Release 2.1

* Wed Oct 03 2018 Robert-André Mauchin <zebob.m@gmail.com> - 2.0-1
- Release 2.0

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 21 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.9-1
- Release 1.9

* Mon Mar 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.8-1
- Release 1.8

* Sat Feb 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.7-1
- First RPM release
