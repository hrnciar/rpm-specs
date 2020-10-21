Summary: InfiniBand fabric simulator for management
Name: ibsim
Version: 0.10
Release: 1%{?dist}
License: GPLv2 or BSD
Source: https://github.com/linux-rdma/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Patch0027: 0027-run_opensm.sh-remove-opensm-c-option.patch

Url: https://github.com/linux-rdma/ibsim
BuildRequires: libibmad-devel, libibumad-devel, gcc

# RDMA is not currently built on 32-bit ARM: #1484155
ExcludeArch: s390 %{arm}

%description
ibsim provides simulation of infiniband fabric for using with
OFA OpenSM, diagnostic and management tools.

%prep
%autosetup -v -p1

%build
%set_build_flags
%make_build

%install
%make_install prefix=%{_prefix} libpath=%{_libdir} binpath=%{_bindir}

%files
%{_libdir}/umad2sim/
%{_bindir}/ibsim
%doc README TODO net-examples scripts
%license COPYING

%changelog
* Thu Oct 08 2020 Honggang Li <honli@redhat.com> -0.10-1
- Rebase to upstream release ibsim-0.10

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 17 2020 Honggang Li <honli@redhat.com> - 0.9-1
- Rebase to upstream release ibsim-0.9

* Sun Feb 09 2020 Honggang Li <honli@redhat.com> - 0.8-4
- Fix FTBFS in Fedora rawhide/f32
- Resolves: bz1799516

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 22 2019 Honggang Li <honli@redhat.com> - 0.8-1
- Import ibsim for fedora
