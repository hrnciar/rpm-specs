Name:       dontpanic   
Version:    1.02
Release:    5%{?dist}
Summary:    Very simple library and executable used in testing Alien::Base
License:    GPL+ or Artistic    
URL:        https://perl5-alien.github.io/page/%{name}.html
Source0:    https://github.com/Perl5-Alien/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make    

%description
This software provides a very simple library and executable used in testing
Alien::Base.

%package devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   pkgconfig

%description devel
This package contains libraries and header files needed for developing
applications that use %{name}.

%prep
%setup -q
autoreconf -fi

%build
%configure --enable-shared --disable-static --disable-silent-rules
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -name '*.la' -delete

%check
make %{?_smp_mflags} check

%files
%license LICENSE
%doc Changes README.md
%{_bindir}/%{name}
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 22 2018 Petr Pisar <ppisar@redhat.com> - 1.02-1
- 1.02 bump

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 07 2017 Petr Pisar <ppisar@redhat.com> - 1.01-2
- Update patch for disabled static linking

* Tue Sep 05 2017 Petr Pisar <ppisar@redhat.com> - 1.01-1
- 1.01 bump

* Fri Sep 01 2017 Petr Pisar <ppisar@redhat.com> - 1.00-1
- 1.00 packaged


