Name:		rocminfo
Version:	1.0.0
Release:	4%{?dist}
Summary:	ROCm system info utility

License:	NCSA
URL:		https://github.com/RadeonOpenCompute/rocminfo
Source0:	https://github.com/RadeonOpenCompute/rocminfo/archive/1.0.0/rocminfo-1.0.0.tar.gz
Patch0:		0001-Fix-rocm-runtime-libdir.patch
Patch1:		0001-Use-CXXFLAGS-defined-in-the-environment.patch
Patch2:		0001-Convert-rocm-agent-enumerator-to-python3.patch
Patch3:		0001-Remove-x86_64-specific-compiler-flags.patch

ExclusiveArch: x86_64 aarch64

BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	rocm-runtime-devel >= 2.0.0
# We need python3-devel for pathfix.py
BuildRequires:	python3-devel

%description
ROCm system info utility


%prep
%autosetup -n %{name}-%{version} -p1

pathfix.py -i %{__python3} rocm_agent_enumerator

%build
mkdir build
cd build
%cmake .. -DROCM_DIR=/usr
%make_build


%install
cd build

mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 rocm_agent_enumerator %{buildroot}%{_bindir}
install -p -m 0755 rocminfo %{buildroot}%{_bindir}

%files
%doc README.md
%license License.txt
%{_bindir}/rocm_agent_enumerator
%{_bindir}/rocminfo


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 16 2019 Tom Stellard <tstellar@redhat.com> - 1.0.0-1
- 1.0.0 Release

