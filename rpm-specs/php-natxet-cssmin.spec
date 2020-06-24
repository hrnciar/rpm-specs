%global github_owner    natxet
%global github_name     CssMin
%global github_version  3.0.6
%global github_commit   d5d9f4c3e5cedb1ae96a95a21731f8790e38f1dd
# if set, will be a post-release snapshot build, otherwise a 'normal' build
#global github_date     20141229
%global shortcommit %(c=%{github_commit}; echo ${c:0:7})
%global packagist_owner natxet
%global packagist_name  CssMin

%global lcname  %(echo %{packagist_name} | tr '[:upper:]' '[:lower:]')

# phpci
%global php_min_ver    5.0.0

Name:           php-%{packagist_owner}-%{lcname}
Version:        %{github_version}
Release:        3%{?github_date:.%{github_date}git%{shortcommit}}%{?dist}
Summary:        Configurable CSS parser and minifier

Group:          Development/Libraries
# License text is included in the sole code file
License:        MIT
URL:            https://github.com/%{github_owner}/%{github_name}
# Must use commit-based not tag-based github tarball:
# https://fedoraproject.org/wiki/Packaging:SourceURL#Github
Source0:        https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{github_name}-%{github_commit}.tar.gz

BuildArch:      noarch
BuildRequires:  php-cli
BuildRequires:  php-pcre

Requires:       php(language) >= %{php_min_ver}
Requires:       php-pcre

Provides:       php-composer(%{packagist_owner}/%{packagist_name}) = %{version}

BuildRequires: %{_bindir}/phpab


%description
CssMin is a css parser and minifier. It minifies css by removing
unneeded whitespace characters, comments, empty blocks and empty
declarations. In addition declaration values can get rewritten to
shorter notation if available. The minification is configurable. 


%prep
%setup -qn %{github_name}-%{github_commit}


%build
# From composer.json, "autoload": {
 #        "classmap": ["src/"]
 %{_bindir}/phpab --quiet --nolower --output ./autoload.php ./


%install
mkdir -p %{buildroot}%{_datadir}/php/%{packagist_owner}/%{packagist_name}
cp -pr src/ %{buildroot}%{_datadir}/php/%{packagist_owner}/%{packagist_name}
cp -p autoload.php %{buildroot}%{_datadir}/php/%{packagist_owner}/%{packagist_name}


%check
# Minimal test for our autoloader
php -r '
  require "%{buildroot}%{_datadir}/php/%{packagist_owner}/%{packagist_name}/autoload.php";
  exit(class_exists("CssMin") ? 0 : 1);
'


%files
%doc README composer.json
%{_datadir}/php/%{packagist_owner}


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 26 2019 Remi Collet <remi@remirepo.net> - 3.0.6-1
- update to 3.0.6
- add minimal test for our autoloader

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Apr 25 2016 James Hogarth <james.hogarth@gmail.com> - 3.0.4-1
- new release 3.0.4
- Add simple classmap autoloader 

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 Adam Williamson <awilliam@redhat.com> - 3.0.3-1
- new release 3.0.3

* Mon Feb 23 2015 Adam Williamson <awilliam@redhat.com> - 3.0.2-2.20141229git8883d28
- change layout to match upstream's (with the /src sub-directory)

* Mon Dec 29 2014 Adam Williamson <awilliam@redhat.com> - 3.0.2-1.20141229git8883d28
- initial package
