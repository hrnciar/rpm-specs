%global opencsd_tag 957d18219d162f52ebe2426f32a4263ec10f357d

Name:           opencsd
Version:        0.14.3
Release:        1%{?dist}
Summary:        An open source CoreSight(tm) Trace Decode library

License:        BSD
URL:            https://github.com/Linaro/OpenCSD
Source0:        https://github.com/Linaro/OpenCSD/archive/%{opencsd_tag}.tar.gz

BuildRequires:  patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  make

%description
This library provides an API suitable for the decode of ARM(r)
CoreSight(tm) trace streams.

%package devel
Summary: Development files for the CoreSight(tm) Trace Decode library
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The opencsd-devel package contains headers and libraries needed
to develop CoreSight(tm) trace decoders.

%prep
%setup -q -n OpenCSD-%{opencsd_tag}

%build
cd decoder/build/linux
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS"
LIB_PATH=%{_lib} make %{?_smp_mflags}


%install
cd decoder/build/linux
PREFIX=%{buildroot}%{_prefix} LIB_PATH=%{_lib} make install DISABLE_STATIC=1 DEF_SO_PERM=755


%check
# no upstream unit tests yet

%files
%license LICENSE
%doc HOWTO.md README.md
%{_libdir}/*so\.*
%{_bindir}/*

%files devel
%doc decoder/docs/prog_guide/*
%{_includedir}/*
# no man files..
%{_libdir}/*so

#------------------------------------------------------------------------------
%changelog
* Wed Sep 23 2020 Jeremy Linton <jeremy.linton@arm.com> - 0.14.3-1
- Update to upstream 0.14.3

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 08 2020 Jeremy Linton <jeremy.linton@arm.com> - 0.14.1-1
- First opencsd package
