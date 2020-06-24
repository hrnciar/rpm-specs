Summary: Strong GPG verification of git tags
Name: git-evtag
Version: 2016.1
Release: 14%{?dist}

License: LGPLv2+
#VCS: https://github.com/cgwalters/git-evtag
URL: https://github.com/cgwalters/git-evtag
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc

# We always run autogen.sh
BuildRequires: autoconf automake libtool

BuildRequires: pkgconfig(libgit2)
BuildRequires: pkgconfig(gio-2.0)

Requires: git
Requires: gnupg2

%description
git-evtag wraps "git tag" functionality, adding stronger checksums
that cover the complete content.

%prep
%autosetup

%build
env NOCONFIGURE=1 ./autogen.sh
%configure --disable-silent-rules
%make_build

%install
%make_install INSTALL="install -p"

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}

%changelog
* Wed Apr 15 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2016.1-14
- Rebuild for libgit2 1.0.0

* Tue Mar 03 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2016.1-13
- Rebuild for libgit2 0.99

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2016.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2016.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 06 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2016.1-10
- Rebuild for libgit2 0.28.x

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2016.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2016.1-8
- Rebuild for libgit2 0.27.x

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2016.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2016.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 08 2017 Igor Gnatenko <ignatenko@redhat.com> - 2016.1-3
- Rebuild for libgit2 0.26.x

* Tue Jan 10 2017 Igor Gnatenko <ignatenko@redhat.com> - 2016.1-2
- Rebuild for libgit2-0.25.x

* Sun Nov 20 2016 Colin Walters <walters@verbum.org> - 2016.1-1
- Initial package
