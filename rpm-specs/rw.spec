Name:		rw
Summary:	Program that calculates rank-width and rank-decompositions
Version:	0.7
Release:	11%{?dist}
License:	GPLv2+
URL:		http://pholia.tdi.informatik.uni-frankfurt.de/~philipp/software/%{name}.shtml
Source0:	http://pholia.tdi.informatik.uni-frankfurt.de/~philipp/software/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:	igraph-devel

%description
rw is a program that calculates rank-width and rank-decompositions.
It is based on ideas from "Computing rank-width exactly" by Sang-il Oum,
"Sopra una formula numerica" by Ernesto Pascal, "Generation of a Vector
from the Lexicographical Index" by B.P. Buckles and M. Lybanon and
"Fast additions on masked integers" by Michael D. Adams and David S. Wise.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
This package contains the header files and development documentation
for %{name}.

%prep
%setup -q

%build
%configure --disable-static

# Get rid of undesirable hardcoded rpaths
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -i libtool

# Avoid f23 make going oom on i386
%if 0%{?fedora} < 24
make
%else
make %{?_smp_mflags}
%endif

%install
make install DESTDIR="%{buildroot}"
rm %{buildroot}%{_libdir}/*.la

# It already installs docs in proper directory
# avoid duplicate entries in $files
cp -p AUTHORS NEWS %{buildroot}%{_docdir}/%{name}/

%ldconfig_scriptlets

%files
%license COPYING
%doc %{_docdir}/%{name}/
%{_bindir}/rw
%{_libdir}/lib%{name}.so.*

%files		devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov  2 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.7-1
- Initial rw spec.
