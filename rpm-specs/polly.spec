#%%global rc_ver 6
%global baserelease 1
%global polly_srcdir polly-%{version}%{?rc_ver:rc%{rc_ver}}.src

Name: polly
Version: 10.0.0
Release: %{baserelease}%{?rc_ver:.rc%{rc_ver}}%{?dist}
Summary: LLVM Framework for High-Level Loop and Data-Locality Optimizations

License: NCSA
URL: http://polly.llvm.org	
%if 0%{?rc_ver:1}
Source0: https://prereleases.llvm.org/%{version}/rc%{rc_ver}/%{polly_srcdir}.tar.xz
Source1: https://prereleases.llvm.org/%{version}/rc%{rc_ver}/%{polly_srcdir}.tar.xz.sig
%else
Source0: https://github.com/llvm/llvm-project/releases/download/llvmorg-%{version}/%{polly_srcdir}.tar.xz
Source3: https://github.com/llvm/llvm-project/releases/download/llvmorg-%{version}/%{polly_srcdir}.tar.xz.sig
%endif
Source2: https://prereleases.llvm.org/%{version}/hans-gpg-key.asc

Patch0: polly-subproject-extension.patch

BuildRequires: cmake
BuildRequires: llvm-devel = %{version}
BuildRequires: llvm-test = %{version}
BuildRequires: clang-devel = %{version}
BuildRequires: python3-lit
BuildRequires: python3-sphinx

%description
Polly is a high-level loop and data-locality optimizer and optimization
infrastructure for LLVM. It uses an abstract mathematical representation based
on integer polyhedron to analyze and optimize the memory access pattern of a
program.

%package devel
Summary: Polly header files
Requires: %{name} = %{version}-%{release}

%description devel
Polly header files.

%package doc
Summary: Documentation for Polly
BuildArch: noarch
Requires: %{name} = %{version}-%{release}

%description doc
Documentation for the Polly optimizer.

%prep
%autosetup -n %{polly_srcdir} -p1

%build
mkdir -p _build
cd _build

%cmake .. \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DLLVM_LINK_LLVM_DYLIB:BOOL=ON \
	-DLLVM_EXTERNAL_LIT=%{_bindir}/lit \
	-DCMAKE_PREFIX_PATH=%{_libdir}/cmake/llvm/ \
\
	-DLLVM_ENABLE_SPHINX:BOOL=ON \
	-DSPHINX_WARNINGS_AS_ERRORS=OFF \
	-DSPHINX_EXECUTABLE=%{_bindir}/sphinx-build-3 \
\
%if 0%{?__isa_bits} == 64
	-DLLVM_LIBDIR_SUFFIX=64
%else
	-DLLVM_LIBDIR_SUFFIX=
%endif



%make_build
%{__make} docs-polly-html


%install
%make_install -C _build
install -d %{buildroot}%{_pkgdocdir}/html
cp -r _build/docs/html/* %{buildroot}%{_pkgdocdir}/html/

%check
%{__make} check-polly -C _build


%files
%{_libdir}/LLVMPolly.so
%{_libdir}/libPolly.so.*
%{_libdir}/libPollyISL.so
%{_libdir}/libPollyPPCG.so

%files devel
%{_libdir}/libPolly.so
%{_includedir}/polly
%{_libdir}/cmake/polly

%files doc
%doc %{_pkgdocdir}/html

%changelog
* Mon Mar 30 2020 sguelton@redhat.com - 10.0.0-1
- llvm-10.0.0 final

* Wed Mar 25 2020 sguelton@redhat.com - 10.0.0-0.2.rc6
- llvm-10.0.0 rc6

* Sat Mar 21 2020 sguelton@redhat.com - 10.0.0-0.1.rc5
- Initial version.

