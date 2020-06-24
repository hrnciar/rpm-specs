Name:       js-jquery-file-upload
Version:    10.13.0
Release:    1%{?dist}
BuildArch:  noarch

License:    MIT
Summary:    File Upload widget for jQuery
URL:        https://github.com/blueimp/jQuery-File-Upload
Source0:    %{url}/archive/v%{version}/jQuery-File-Upload-%{version}.tar.gz

BuildRequires: closure-compiler
BuildRequires: web-assets-devel

Requires:      js-jquery >= 1.6.0
Requires:      js-jquery-iframe-transport
Requires:      web-assets-filesystem
Requires:      xstatic-jquery-ui-common


%description
File Upload widget with multiple file selection, drag&drop support, progress
bars, validation and preview images, audio and video for jQuery.
Supports cross-domain, chunked and resumable file uploads and client-side
image resizing. Works with any server-side platform (PHP, Python, Ruby on
Rails, Java, Node.js, Go etc.) that supports standard HTML form file uploads.


%prep
%autosetup -n jQuery-File-Upload-%{version}

# We must minify the JS ourselves.
find . -name "*.min.js" -delete

# Don't use bundled libraries
rm js/jquery.iframe-transport.js
rm js/vendor/jquery.ui.widget.js


%build
ln -s /usr/share/javascript/jquery-iframe-transport/jquery.iframe-transport.js \
    js/jquery.iframe-transport.js
ln -s /usr/share/javascript/jquery_ui/ui/jquery.ui.widget.js js/vendor/jquery.ui.widget.js


%install
install -d -m 0755 %{buildroot}/%{_webassetdir}
install -d -m 0755 %{buildroot}/%{_webassetdir}/jQuery-File-Upload
install -d -m 0755 %{buildroot}/%{_webassetdir}/jQuery-File-Upload/cors
install -d -m 0755 %{buildroot}/%{_webassetdir}/jQuery-File-Upload/css
install -d -m 0755 %{buildroot}/%{_webassetdir}/jQuery-File-Upload/img
install -d -m 0755 %{buildroot}/%{_webassetdir}/jQuery-File-Upload/js

cp -a *.html cors css img js %{buildroot}/%{_webassetdir}/jQuery-File-Upload


%files
%license LICENSE.txt
%doc README.md
%{_webassetdir}/jQuery-File-Upload


%changelog
* Sat Apr 11 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 10.13.0-1
- Update to 10.13.0 (#1823106)

* Fri Apr 10 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 10.12.0-1
- Update to 10.12.0 (#1784595)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 24 2019 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 10.4.0-1
- Update to 10.4.0 (#1768204)

* Tue Sep 03 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 10.2.0-1
- Update to 10.2.0 (#1723177).
- https://github.com/blueimp/jQuery-File-Upload/compare/v9.34.0...v10.2.0

* Tue Sep 03 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 9.34.0-1
- Update to 9.34.0 (#1723177).
- https://github.com/blueimp/jQuery-File-Upload/compare/v9.31.0...v9.34.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.31.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 9.31.0-1
- Update to 9.31.0 (#1700322).
- https://github.com/blueimp/jQuery-File-Upload/compare/v9.22.0...v9.31.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 17 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 9.22.0-1
- Update to 9.22.0 (#1592837).
- https://github.com/blueimp/jQuery-File-Upload/compare/v9.21.0...v9.22.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9.21.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 9.21.0-1
- Update to 9.21.0 (#1548605).

* Mon Feb 12 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 9.20.0-1
- Update to 9.20.0 (#1436897).

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
