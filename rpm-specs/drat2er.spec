%global gitdate 20190307
%global commit 521caf16149df3dfa46f700ec1fab56f8cc12a18
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           drat2er
Version:        0
Release:        0.3.%{gitdate}.%{shortcommit}%{?dist}
Summary:        Proof transformer for propositional logic

License:        MIT
URL:            https://github.com/alex-ozdemir/drat2er/
Source0:        https://github.com/alex-ozdemir/drat2er/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# Unbundle the third-party libraries
Patch0:         %{name}-unbundle.patch
# Build a shared library instead of a static library
Patch1:         %{name}-shared.patch
# Fix a C++ assertion failure due to calling front() on an empty string
Patch2:         %{name}-string-front.patch
# Fix drat-trim problems caused by passing arguments in the wrong order.
# Drat-trim does all actions associated with a command line argument before
# processing the next one.  Therefore, the verbosity option must come first.
Patch3:         %{name}-arg-order.patch

BuildRequires:  catch-devel
BuildRequires:  cli11-static
BuildRequires:  cmake
BuildRequires:  drat-trim-devel
BuildRequires:  drat-trim-tools
BuildRequires:  gcc-c++
BuildRequires:  help2man

%description
Drat2er is a tool for transforming proofs that are usually produced by
SAT solvers.  It takes as input a propositional formula (specified in
the DIMACS format) together with a DRAT proof (DRAT is the current
standard format for proofs in SAT solving), and outputs an
extended-resolution proof of the formula in either the TRACECHECK or
the DRAT format.  The details of this proof transformation are
described in the paper "Extended Resolution Simulates DRAT" (IJCAR
2018).  Note that if drat2er is given as input a DRUP proof, then it
transforms this DRUP proof into an ordinary resolution proof.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers files and library links for developing applications that use
%{name}.

%package        tools
Summary:        Command line interface to %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tools
This package contains a command line interface to %{name}.

%prep
%autosetup -p0 -n %{name}-%{commit}

# Fix the library directory name on 64-bit systems
if [ "%{_lib}" = "lib64" ]; then
  sed -i 's,{CMAKE_BINARY_DIR}/lib,&64,g' CMakeLists.txt
fi

# Do not use the bundled libraries
rm -fr third-party

%build
%cmake -DCMAKE_SKIP_RPATH:BOOL=YES -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES .
%make_build
export LD_LIBRARY_PATH=$PWD/%{_lib}
help2man --version-string=%{gitdate} -N -o %{name}.1 bin/%{name}

%install
# Install the library
mkdir -p %{buildroot}%{_libdir}
cp -a %{_lib}/lib%{name}* %{buildroot}%{_libdir}

# Install the headers
mkdir -p %{buildroot}%{_includedir}/%{name}
cp -p include/drat* %{buildroot}%{_includedir}/%{name}

# Install the binary
mkdir -p %{buildroot}%{_bindir}
cp -p bin/%{name} %{buildroot}%{_bindir}

# Install the man page
mkdir -p %{buildroot}%{_mandir}/man1
cp -p %{name}.1 %{buildroot}%{_mandir}/man1

%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} make test

%files
%license LICENSE
%{_libdir}/lib%{name}.so.0
%{_libdir}/lib%{name}.so.0.*

%files          devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so

%files          tools
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20190307.521caf1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20190307.521caf1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun  6 2019 Jerry James <loganjerry@gmail.com> - 0-0.1.20190307.521caf1
- Initial RPM
