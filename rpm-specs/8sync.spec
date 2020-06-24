%global debug_package %{nil}

Summary:         Asynchronous programming library for GNU Guile
Name:            8sync
Version:         0.4.2
Release:         9%{?dist}
Source:          ftp://ftp.gnu.org/gnu/8sync/8sync-%{?version}.tar.gz
URL:             https://www.gnu.org/software/8sync
License:         LGPLv3+

BuildRequires:   guile22-devel
BuildRequires:   texinfo

%description
8sync (pronounced "eight-sync") is an asynchronous programming library for GNU
Guile. Based on the actor model, it makes use of delimited continuations to
avoid a mess of callbacks resulting in clean, easy to read non-blocking code.

8sync also aims to be batteries included.


%prep
%autosetup


%build

%configure GUILE_TOOLS='/usr/bin/guile-tools2.2' \
           GUILE_CONFIG='/usr/bin/guile-config2.2' \
           GUILD='/usr/bin/guild2.2' \
           GUILE='/usr/bin/guile2.2'

%make_build


%install
%make_install

rm -rf $RPM_BUILD_ROOT%{_datadir}/info/dir

%postun
/sbin/ldconfig

%files
%doc NEWS README
%license COPYING
%license COPYING-gplv3.txt
%{_libdir}/guile/2.2/ccache/8sync.go
%{_libdir}/guile/2.2/ccache/8sync
%{_datadir}/guile/site/2.2/8sync.scm
%{_datadir}/guile/site/2.2/8sync
%{_datadir}/info/8sync.info.gz

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 17 2017 John Dulaney <jdulaney@Fedoraproject.org> - 0.4.2-4
- Initial build

* Wed Nov 15 2017 John Dulaney <jdulaney@Fedoraproject.org> - 0.4.2-3
- Prepare for package review

* Tue Apr 11 2017 John Dulaney <jdulaney@Fedoraproject.org> - 0.4.2-2
- Remove /usr/share/info/dir

* Tue Mar 21 2017 John Dulaney <jdulaney@Fedoraproject.org> - 0.4.2-1
- Initial packaging.
