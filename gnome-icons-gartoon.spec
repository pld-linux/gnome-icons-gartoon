#
%define realname gartoon
#
Summary:	Gartoon Gnome Icons
Summary(pl):	Zestaw ikonek Gartoon dla Gnome
Name:		gnome-icons-gartoon
Version:	0.5
Release:	0.1
Epoch:		0
License:	GPL v2
Group:		X11/Amusements
Source0:	http://zeus.qballcow.nl/icon/paket/%{realname}-%{version}.tar.gz
# Source0-md5:	19fd88682ad2f88ca85f7e0a904610fd
URL:		http://zeus.qballcow.nl/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gartoon is a fun looking icon pack for GNOME desktop environment.

%description -l pl
Gartoon jest zestawem śmiesznie wyglądających ikonek dla GNOME.

%prep
%setup -q -n %{realname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}/%{realname}
install -d $RPM_BUILD_ROOT%{_iconsdir}/%{realname}/scalable/apps
install -d $RPM_BUILD_ROOT%{_iconsdir}/%{realname}/scalable/devices
install -d $RPM_BUILD_ROOT%{_iconsdir}/%{realname}/scalable/emblems
install -d $RPM_BUILD_ROOT%{_iconsdir}/%{realname}/scalable/filesystems
install -d $RPM_BUILD_ROOT%{_iconsdir}/%{realname}/scalable/mimetypes
install -d $RPM_BUILD_ROOT%{_iconsdir}/%{realname}/scalable/stock/Xtra

install index.theme $RPM_BUILD_ROOT%{_iconsdir}/%{realname}
install scalable/apps/*.svg $RPM_BUILD_ROOT%{_iconsdir}/%{realname}/scalable/apps
install scalable/devices/*.svg $RPM_BUILD_ROOT%{_iconsdir}/%{realname}/scalable/devices
install scalable/emblems/*.svg $RPM_BUILD_ROOT%{_iconsdir}/%{realname}/scalable/emblems
install scalable/emblems/*.icon $RPM_BUILD_ROOT%{_iconsdir}/%{realname}/scalable/emblems
install scalable/filesystems/*.svg $RPM_BUILD_ROOT%{_iconsdir}/%{realname}/scalable/filesystems
install scalable/filesystems/*.icon $RPM_BUILD_ROOT%{_iconsdir}/%{realname}/scalable/filesystems
install scalable/mimetypes/*.svg $RPM_BUILD_ROOT%{_iconsdir}/%{realname}/scalable/mimetypes
install scalable/stock/*.svg $RPM_BUILD_ROOT%{_iconsdir}/%{realname}/scalable/stock
install scalable/stock/iconrc $RPM_BUILD_ROOT%{_iconsdir}/%{realname}/scalable/stock
install scalable/stock/Xtra/*.svg $RPM_BUILD_ROOT%{_iconsdir}/%{realname}/scalable/stock/Xtra

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README gartoon-pallete.svg
%dir %{_iconsdir}/%{realname}
%dir %{_iconsdir}/%{realname}/scalable
%dir %{_iconsdir}/%{realname}/scalable/apps
%dir %{_iconsdir}/%{realname}/scalable/devices
%dir %{_iconsdir}/%{realname}/scalable/emblems
%dir %{_iconsdir}/%{realname}/scalable/filesystems
%dir %{_iconsdir}/%{realname}/scalable/mimetypes
%dir %{_iconsdir}/%{realname}/scalable/stock
%dir %{_iconsdir}/%{realname}/scalable/stock/Xtra
%{_iconsdir}/%{realname}/index.theme
%{_iconsdir}/%{realname}/scalable/apps/*.svg
%{_iconsdir}/%{realname}/scalable/devices/*.svg
%{_iconsdir}/%{realname}/scalable/emblems/*.svg
%{_iconsdir}/%{realname}/scalable/emblems/*.icon
%{_iconsdir}/%{realname}/scalable/filesystems/*.svg
%{_iconsdir}/%{realname}/scalable/filesystems/*.icon
%{_iconsdir}/%{realname}/scalable/mimetypes/*.svg
%{_iconsdir}/%{realname}/scalable/stock/*.svg
%{_iconsdir}/%{realname}/scalable/stock/Xtra/*.svg
%{_iconsdir}/%{realname}/scalable/stock/iconrc
