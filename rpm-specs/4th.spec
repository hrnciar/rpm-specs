Name:           4th
Version:        3.62.5
Release:        6%{?dist}
Summary:        A Forth compiler

License:        GPLv3+
URL:            https://thebeez.home.xs4all.nl/4tH/
Source0:        https://downloads.sourceforge.net/project/forth-4th/%{name}-%{version}/%{name}-%{version}-unix.tar.gz

BuildRequires:  gcc make

%description
4tH is basic framework for creating application specific scripting
languages. It is a library of functions centered around a virtual
machine, which guarantees high performance, ease of use and low overhead.


%package devel
Summary:        Development files for 4th
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package includes headers for development with 4th, a Forth compiler
library.


%prep
%setup -q -n %{name}-%{version}-unix


%build
LD_LIBRARY_PATH="$PWD/sources/" \
make %{?_smp_mflags} -C sources \
        STATIC= SHARED=1 \
        CFLAGS="-DUNIX -fsigned-char %{optflags} -fPIC"


%install
mkdir -p \
        %{buildroot}%{_libdir} \
        %{buildroot}%{_includedir}/%{name} \
        %{buildroot}%{_bindir} \
        %{buildroot}%{_mandir} \
        %{buildroot}%{_docdir}/%{name}

LD_LIBRARY_PATH="$PWD/sources/" \
%make_install -C sources \
        STATIC= SHARED=1 \
        LIBRARIES=%{buildroot}%{_libdir} \
        INCLUDES=%{buildroot}%{_includedir} \
        BINARIES=%{buildroot}%{_bindir} \
        MANDIR=%{buildroot}%{_mandir} \
        DOCDIR=%{buildroot}%{_docdir}
cp -ap sources/include/*.h %{buildroot}%{_includedir}/%{name}/


%files
%{_libdir}/lib4th.so.3*
%{_bindir}/4tsh
%{_bindir}/pp4th
%{_bindir}/4th
%{_mandir}/man1/4th.1*
%doc %{_docdir}/%{name}
%doc README
%license COPYING


%files devel
%{_libdir}/lib4th.so
%{_includedir}/%{name}


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.62.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.62.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.62.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.62.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 16 2018 Lubomir Rintel <lkundrak@v3.sk> - 3.62.5-2
- Fix issues discovered in review (Robert-André Mauchin, rh#1628149):
- Dropped Group tag
- Fixed a typo in devel package requires
- Corrected the dynamic library file match

* Tue Sep 11 2018 Lubomir Rintel <lkundrak@v3.sk> - 3.62.5-1
- Initial packaging
