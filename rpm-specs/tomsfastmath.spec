%global ver_maj 0
%global ver_min 13
%global ver_patch 1
Name:		tomsfastmath
Version:	%{ver_maj}.%{ver_min}.%{ver_patch}
Release:	7%{?dist}
Summary:	Fast large integer arithmetic library

License:	Public Domain or WTFPL
URL:		http://www.libtom.net/
Source0:	https://github.com/libtom/tomsfastmath/archive/v%{ver_maj}.%{ver_min}.%{ver_patch}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:	libtool
BuildRequires:	gcc

%description
TomsFastMath is meant to be a very fast yet still fairly portable and easy to
port large integer arithmetic library written in ISO C. The goal specifically
is to be able to perform very fast modular exponentiations and other related
functions required for ECC, DH and RSA cryptosystems.

%package devel
Summary:	Development headers for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development headers for %{name}

%prep
%setup -q

%build
%make_build -f makefile.shared CFLAGS="%{build_cflags} -fomit-frame-pointer -Isrc/headers" LDFLAGS="%{build_ldflags}"

%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
install -p -m0755 .libs/libtfm.so.1.0.0 %{buildroot}%{_libdir}
pushd %{buildroot}%{_libdir}
ln -s libtfm.so.1.0.0 libtfm.so.1
ln -s libtfm.so.1.0.0 libtfm.so
popd
install -p -m0644 -D src/headers/tfm.h %{buildroot}%{_includedir}
# Add tomsfastmath.pc in next release
# sed -e 's,^Version:.*,Version: %%{version},' tomsfastmath.pc.in > tomsfastmath.pc
# mkdir -p %%{buildroot}%%{_libdir}/pkgconfig
# install -p -m 0644 -D tomsfastmath.pc %%{buildroot}%%{_libdir}/pkgconfig/

%ldconfig_scriptlets

%files
%doc doc/tfm.pdf
%license LICENSE
%{_libdir}/libtfm.so.*

%files devel
%{_includedir}/tfm.h
%{_libdir}/libtfm.so

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Tomas Korbar <tomas.korb@seznam.cz> - 0.13.1-3
- Add gcc to build requires

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 20 2018 Tomas Korbar <tomas.korb@seznam.cz> 0.13.1-1
- Initial import (#1567898)
