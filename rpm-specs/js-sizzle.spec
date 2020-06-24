# this is the 2.1.1-jquery.2.1.2 tag on github
%global commit 2280ab78b0e19dc494f9c47fd1f4a42dd63c280d
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           js-sizzle
Version:        2.1.1
Release:        10.jquery.2.1.2%{?dist}
Summary:        A pure-JavaScript CSS selector engine
BuildArch:      noarch

%global ver_x %(echo %{version} | cut -d. -f1)
%global ver_y %(echo %{version} | cut -d. -f2)
%global ver_z %(echo %{version} | cut -d. -f3)

License:        MIT     
URL:            http://sizzlejs.com/
Source0:        https://github.com/jquery/sizzle/archive/%{commit}/%{name}-%{commit}.tar.gz

# disable gzip-js during build
Patch1:         %{name}-disable-gzip-js.patch

BuildRequires:  web-assets-devel
BuildRequires:  nodejs-packaging

Provides:       %{name}-static = %{version}-%{release}

# for the benefit of those installing the review, will drop when importing
Obsoletes:      %{name}-source < %{version}

BuildRequires:  nodejs-grunt >= 0.4.4-3
BuildRequires:  npm(grunt-cli)
BuildRequires:  npm(grunt-contrib-uglify)
BuildRequires:  npm(load-grunt-tasks)

Requires:       web-assets-filesystem

%description
A pure-JavaScript CSS selector engine designed to be easily dropped in to a host
library.

%prep
%setup -qn sizzle-%{commit}
%patch1 -p1

#remove precompiled stuff
rm -rf dist/*


%build
%nodejs_symlink_deps --build
grunt -v compile uglify


# missing dependencies
#%%check
#grunt


%install
%global inslibdir %{buildroot}%{_jsdir}/sizzle

mkdir -p %{inslibdir}/%{version}
cp -p dist/* %{inslibdir}/%{version}

ln -s %{version} %{inslibdir}/latest
ln -s %{version} %{inslibdir}/%{ver_x}
ln -s %{version} %{inslibdir}/%{ver_x}.%{ver_y}

%files
%{_jsdir}/sizzle
%doc AUTHORS.txt CONTRIBUTING.md LICENSE.txt README.md


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-10.jquery.2.1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-9.jquery.2.1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-8.jquery.2.1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-7.jquery.2.1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-6.jquery.2.1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-5.jquery.2.1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-4.jquery.2.1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3.jquery.2.1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-2.jquery.2.1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 04 2015 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.1.1-1
- new upstream release 2.1.1-jquery2.1.2

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jun 03 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.10.19-3
- follow the github SourceURL guidelines

* Sat May 31 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.10.19-2
- drop sed hack now that grunt is fixed

* Fri May 30 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.10.19-1
- update to 1.10.19
- use system packages for build

* Wed Mar 19 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.10.16-0.1
- initial package
