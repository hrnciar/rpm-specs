Name:           tasksh
Version:        1.2.0
Release:        7%{?dist}
Summary:        Shell command that wraps Taskwarrior commands

License:        MIT
URL:            https://taskwarrior.org/
Source0:        https://taskwarrior.org/download/%{name}-%{version}.tar.gz
# We install docs ourselves
Patch0:         0001-don-t-install-docs.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  readline-devel
Requires:       task

%description
Tasksh is a shell command that wraps Taskwarrior commands. It is intended to
provide simpler Taskwarrior access, and add a few new features of its own.

Tasksh replaces the built-in shell command of older releases, and the bundled
tasksh program of version 2.3.0. The former was very limited and the latter
unsupported, buggy and flawed.

%prep
%autosetup -p1

%build
mkdir %{_target_platform}
pushd %{_target_platform}
  %cmake .. -DCMAKE_BUILD_TYPE=RelWithDebInfo
popd
%make_build -C %{_target_platform}

%install
%make_install -C %{_target_platform}

%files
%license LICENSE
%doc ChangeLog AUTHORS NEWS
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.0-5
- Rebuild for readline 8.0

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 02 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0

* Thu Dec 01 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.1.0-1
- Initial package
