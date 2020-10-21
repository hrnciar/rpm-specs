Name: cvise
Version: 1.4.0
Release: 4%{?dist}
Summary: Super-parallel Python port of the C-Reduce
License: BSD
URL: https://github.com/marxin/cvise
Source: https://github.com/marxin/cvise/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: astyle
BuildRequires: cmake
BuildRequires: flex
BuildRequires: llvm-devel
BuildRequires: unifdef
BuildRequires: clang-devel
BuildRequires: indent
BuildRequires: gcc-c++
BuildRequires: python3-pebble
BuildRequires: python3-pytest
BuildRequires: python3-psutil
Requires: astyle
Requires: clang
Requires: unifdef
Requires: python3-pebble
Requires: python3-psutil
Requires: indent

%description
C-Vise is a super-parallel Python port of the C-Reduce. The port is fully
compatible to the C-Reduce and uses the same efficient
LLVM-based C/C++ reduction tool named clang_delta.

C-Vise is a tool that takes a large C, C++ or OpenCL program that
has a property of interest (such as triggering a compiler bug) and
automatically produces a much smaller C/C++ or OpenCL program that
has the same property. It is intended for use by people who discover
and report bugs in compilers and other tools that process C/C++ or OpenCL code.

%prep
%setup -q

%build
# Fedora says we shouldn't put files in /usr/local/.
mkdir objdir && cd objdir && \
%cmake .. \
  -B %{_target_platform} \
  -DCMAKE_INSTALL_LIBEXECDIR=%{_libexecdir} \
  -DCMAKE_INSTALL_BINDIR=%{_bindir} \
  -DCMAKE_INSTALL_DATADIR=%{_datadir} \
  -DCMAKE_BUILD_TYPE=$BUILD_TYPE \
  -DCMAKE_SKIP_RPATH=TRUE && \
%make_build VERBOSE=1 -C %{_target_platform}

%check
cd objdir && pytest

%install
%make_install -C objdir/%{_target_platform}

%files
%license COPYING
%{_bindir}/cvise
%{_bindir}/cvise-delta
%dir %{_libexecdir}/cvise
%{_libexecdir}/cvise/clex
%{_libexecdir}/cvise/clang_delta
%{_libexecdir}/cvise/strlex
%{_libexecdir}/cvise/topformflat
%{_datadir}/cvise

%changelog
* Mon Aug 03 2020 Marek Polacek <polacek@redhat.com> - 1.4.0-4
- Use the _target_platform directory when building/installing (#1863387)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Marek Polacek <polacek@redhat.com> - 1.4.0-1
- initial version
