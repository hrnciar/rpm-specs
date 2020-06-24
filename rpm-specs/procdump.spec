# Name of the upstream GitHub repository.
%global repo_name ProcDump-for-Linux

Name:           procdump
Version:        1.1.1
Release:        1%{?dist}
Summary:        Sysinternals process dump utility

License:        MIT
URL:            https://github.com/microsoft/%{repo_name}
Source:         %{url}/archive/%{version}/%{repo_name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  zlib-devel
Requires:       gdb >= 7.6.1

# Fix for GCC 10 (Fedora 32) builds
# https://github.com/microsoft/ProcDump-for-Linux/pull/79
Patch0:         0001-Fix-for-build-on-GCC-10.patch

%description
ProcDump is a command-line utility whose primary purpose is monitoring an
application for various resources and generating crash dumps during a spike that
an administrator or developer can use to determine the cause of the issue.
ProcDump also serves as a general process dump utility that you can embed in
other scripts.


%prep
%autosetup -p1 -n %{repo_name}-%{version}


%build
%make_build CFLAGS="%{optflags}"


%install
%make_install


%files
%license LICENSE
%doc README.md
%doc procdump.gif
%{_bindir}/procdump
%{_mandir}/man1/procdump.1*



%changelog
* Sat Apr 04 2020 Matěj Grabovský <mgrabovs@redhat.com> - 1.1.1-1
- Added -T thread count trigger and -F file descriptor count trigger

* Thu Feb 20 2020 Matěj Grabovský <mgrabovs@redhat.com> - 1.1-3
- Fix build with GCC 10

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Matěj Grabovský <mgrabovs@redhat.com> - 1.1-1
- Add command line parameter (-w) for targetting the name of a process
- Small bug fixes

* Fri Oct 4 2019 Matěj Grabovský <mgrabovs@redhat.com> - 1.0.1-1
- Initial release
